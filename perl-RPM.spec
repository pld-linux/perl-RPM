%include	/usr/lib/rpm/macros.perl
Summary:	Native bindings to the RPM Package Manager API for Perl
Summary(pl):	Modu� perla RPM
Name:		perl-RPM
Version:	0.40
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/RPM/Perl-RPM-%{version}.tar.gz
Patch0:		%{name}-old-include.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpm-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Perl-RPM

%description
RPM perl module.

%description -l pl
Modu� perla RPM.

%prep
%setup -q -n Perl-RPM-%{version}
%patch0 -p1

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
%{perl_sitearch}/auto/RPM
%{_mandir}/man[13]/*
