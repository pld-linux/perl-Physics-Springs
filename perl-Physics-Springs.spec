#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Physics
%define	pnam	Springs
Summary:	Physics::Springs - Simulate Particle Dynamics with Springs
Summary(pl.UTF-8):	Physics::Springs - symulacja dynamiki cząstek ze sprężynami
Name:		perl-Physics-Springs
Version:	1.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Physics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	092be260863a3d1e941ef1f29a31d0e6
URL:		http://search.cpan.org/dist/Physics-Springs/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Physics-Particles >= 1.00
BuildRequires:	perl-Sub-Assert
BuildRequires:	perl >= 5.006
%endif
Requires:	perl-Physics-Particles >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended as an add-on to the Physics::Particles module
(version 1.00 or higher required) and may be used to simulate particle
dynamics including spring-like forces between any two particles you
specify.

The module extends the API of Physics::Particles by one method. Please
see the documentation to Physics::Particles for more information about
the API.

There are several particle properties required by Physics::Springs in
order to work: These are the x/y/z coordinates, the vx/vy/vz
velocity vector components, and a non-zero mass 'm'. Furthermore, it
uses the _fx, _fy, _fz properties which the user should never modify
directly.

%description -l pl.UTF-8
Ten moduł jest dodatkiem do modułu Physics::Particles (w wersji 1.00
lub wyższej) służącym do symulowania dynamiki cząsek włącznie z siłami
typu sprężynowego pomiędzy dwiema wybranymi cząstkami.

Ten moduł rozszerza API Physics::Particles o jedną metodę. Więcej
informacji o API można znaleźć w tamtym module.

Jest kilka właściwości cząstki wymaganych do działania przez
Physics::Springs - są to: współrzędne x/y/z, składowe wektora
prędkości vz/vy/vz oraz niezerowa masa m. Co więcej, moduł
wykorzystuje właściwości _fx, _fy, _fz, których użytkownik nie
powinien nigdy bezpośrednio zmieniać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Physics/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
