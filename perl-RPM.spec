#
%bcond_with	tests	# perform "make test" (uses rpm database, which must not
			# be broken by gettext-in-header patch)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Native bindings to the RPM Package Manager API for Perl
Summary(pl):	Natywne dowi�zania do API zarz�dcy pakiet�w RPM dla Perla
Name:		perl-RPM
Version:	0.40
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPM/Perl-RPM-%{version}.tar.gz
# Source0-md5:	f15aa29bd0af0e1102d757ce20500f26
Patch0:		%{name}-43.patch
URL:		http://www.blackperl.com/Perl-RPM/
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-devel >= 4.2.1
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
Pakiet Perl-RPM to pr�ba dostarczenia dost�pu z poziomu Perla do
pe�nego interfejsu programistycznego, b�d�cego cz�ci� zarz�dcy
pakiet�w RPM. Zamiast polega� na wywo�ywaniu polece� RPM i
analizowaniu ich wyj�cia, te modu�y pr�buj� dostarczy� programistom
perlowym mo�liwo�� robienia wszystkiego, co musia�oby by� robione w C
lub C++.

%prep
%setup -q -n Perl-RPM-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
