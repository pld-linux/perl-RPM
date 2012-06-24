%include	/usr/lib/rpm/macros.perl
Summary:	Native bindings to the RPM Package Manager API for Perl
Summary(pl):	Natywne dowi�zania do API zarz�dcy pakiet�w RPM
Name:		perl-RPM
Version:	0.40
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/Perl-RPM-%{version}.tar.gz
Patch0:		%{name}-old-include.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-devel
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
Pakiet Perl-RPM to pr�ba dostarczenia dost�pu z poziomu Perla do
pe�nego interfejsu programistycznego, b�d�cego cz�ci� zarz�dcy
pakiet�w RPM. Zamiast polega� na wywo�ywaniu polece� RPM i
analizowaniu ich wyj�cia, te modu�y pr�buj� dostarczy� programistom
perlowym mo�liwo�� robienia wszystkiego, co musia�oby by� robione w C
lub C++.

%prep
%setup -q -n Perl-RPM-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
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
%{perl_sitearch}/RPM.pm
%{perl_sitearch}/RPM
%dir %{perl_sitearch}/auto/RPM
%{perl_sitearch}/auto/RPM/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/RPM/*.so
%{_mandir}/man[13]/*
