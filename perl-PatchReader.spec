%define	upstream_name	 PatchReader
%define upstream_version 0.9.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	13

Summary:	Utilities to read and manipulate patches and CVS 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PatchReader/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
%rename perl-patchreader

%description
This perl library allows you to manipulate patches programmatically by chaining
together a variety of objects that read, manipulate, and output patch
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README
find . -type f -exec perl -pi -e 'tr/\r//d' {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/PatchReader
%{perl_vendorlib}/PatchReader.pm
%{_mandir}/man3/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.9.5-10mdv2010.1
+ Revision: 505284
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.5-9mdv2010.0
+ Revision: 430521
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.5-8mdv2009.0
+ Revision: 241812
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-6mdv2008.0
+ Revision: 47015
- rebuild


* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-5mdv2007.0
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-4mdk 
- really drop useless empty directories

* Mon Jun 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-3mdk 
- fix url
- drop useless empty directories

* Mon May 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-2mdk 
- obsoletes already-existing perl-patchreader (thx titi)
- test in %%check
- fix doc perms
- fix files encoding

* Mon Jan 31 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.9.5-1mdk 
- first mdk release

