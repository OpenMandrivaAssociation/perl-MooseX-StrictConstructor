%define upstream_name    MooseX-StrictConstructor
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Make your object constructors blow up on unknown attributes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
Requires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
Using this class to load Moose instead of just loading using Moose itself
makes your constructors "strict". If your constructor is called with an
attribute init argument that your class does not declare, then it calls
"Carp::confess()". This is a great way to catch small typos.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 659979
- update to new version 0.16

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2
+ Revision: 657480
- add runtime req

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 643533
- update to new version 0.13

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 594879
- update to new version 0.12

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 586770
- new version

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 558784
- new version

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 554006
- adding missing buildrequires:
- update to 0.09

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 404041
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 371863
- new version

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.0
+ Revision: 281109
- update to new version 0.07

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 236380
- import perl-MooseX-StrictConstructor


* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
- initial mdv release, generated with cpan2dist
