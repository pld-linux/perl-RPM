%include	/usr/lib/rpm/macros.perl
Summary:	Native bindings to the RPM Package Manager API for Perl
Summary(pl):	Natywne dowi±zania do API zarz±dcy pakietów RPM
Name:		perl-RPM
Version:	0.40
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/Perl-RPM-%{version}.tar.gz
# Source0-md5:	f15aa29bd0af0e1102d757ce20500f26
Patch0:		%{name}-old-include.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Perl-RPM

%description
The Perl-RPM package is an attempt to provide Perl-level access to the
complete application programming interface that is a part of the RPM
Package Manager (RPM). Rather than have scripts rely on executing RPM
commands and parse the resultant output, this modules aims to provide
Perl programmers the ability to do anything that would otherwise have
been done in C or C++.

%description -l pl
Pakiet Perl-RPM to próba dostarczenia dostêpu z poziomu Perla do
pe³nego interfejsu programistycznego, bêd±cego czê¶ci± zarz±dcy
pakietów RPM. Zamiast polegaæ na wywo³ywaniu poleceñ RPM i
analizowaniu ich wyj¶cia, te modu³y próbuj± dostarczyæ programistom
perlowym mo¿liwo¶æ robienia wszystkiego, co musia³oby byæ robione w C
lub C++.

%prep
%setup -q -n Perl-RPM-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rpmprune
%{perl_vendorarch}/RPM.pm
%{perl_vendorarch}/RPM
%dir %{perl_vendorarch}/auto/RPM
%{perl_vendorarch}/auto/RPM/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RPM/*.so
%{_mandir}/man[13]/*
