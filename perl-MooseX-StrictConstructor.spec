%define module   MooseX-StrictConstructor
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Make your object constructors blow up on unknown attributes
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Using this class to load Moose instead of just loading using Moose itself
makes your constructors "strict". If your constructor is called with an
attribute init argument that your class does not declare, then it calls
"Carp::confess()". This is a great way to catch small typos.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MooseX

