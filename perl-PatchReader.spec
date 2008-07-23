%define	module	PatchReader
%define	name	perl-%{module}
%define version 0.9.5
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Utilities to read and manipulate patches and CVS 
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/PatchReader/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Obsoletes:	perl-patchreader
Provides:	perl-patchreader

%description
This perl library allows you to manipulate patches programmatically by chaining
together a variety of objects that read, manipulate, and output patch
information.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes README
find . -type f -exec perl -pi -e 'tr/\r//d' {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/PatchReader
%{perl_vendorlib}/PatchReader.pm
%{_mandir}/man3/*

