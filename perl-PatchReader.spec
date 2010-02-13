%define	upstream_name	 PatchReader
%define upstream_version 0.9.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 10

Summary:	Utilities to read and manipulate patches and CVS 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PatchReader/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:	perl-patchreader
Provides:	perl-patchreader

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
