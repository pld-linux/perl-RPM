%include	/usr/lib/rpm/macros.perl
Summary:	Native bindings to the RPM Package Manager API for Perl
Summary(pl):	Modu³ perla RPM
Name:		perl-RPM
Version:	0.32
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/RPM/Perl-RPM-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpm-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Perl-RPM

%description
RPM perl module.

%description -l pl
Modu³ perla RPM.

%prep
%setup -q -n Perl-RPM-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rpmprune
%{perl_sitearch}/RPM.pm
%{perl_sitearch}/RPM
%dir %{perl_sitearch}/auto/RPM
%attr(755,root,root) %{perl_sitearch}/auto/RPM/RPM.so
%{_mandir}/man3/*
