#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Physics
%define	pnam	Springs
Summary:	Physics::Springs - Simulate Particle Dynamics with Springs
#Summary(pl):	
Name:		perl-Physics-Springs
Version:	1.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	092be260863a3d1e941ef1f29a31d0e6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Physics::Particles) >= 1.00
BuildRequires:	perl(Sub::Assert)
BuildRequires:	perl >= 5.006
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended as an add-on to the Physics::Particles module
(version 1.00 or higher required) and may be used to simulate particle
dynamics including spring-like forces between any two particles you specify.

Since version 1.00 of this module, Physics::Particles version 1.00 is required.
Version 1.00 is neither compatible to earlier versions nor to any versions
below 1.00 of Physics::Particles and Physics::Springs::Friction.

The module extends the API of Physics::Particles by one method which is
documented below. Please see the documentation to Physics::Particles for
more information about the API.

There are several particle properties required by Physics::Springs in
order to work: These are the x/y/z coordinates, the vx/vy/vz
velocity vector components, and a non-zero mass 'm'. Furthermore, it uses
the _fx, _fy, _fz properties which the user should never modify directly.



# %description -l pl
# TODO

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
#%{perl_vendorlib}/Physics/Springs
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
