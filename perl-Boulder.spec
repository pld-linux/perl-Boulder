#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Boulder - an API for hierarchical tag/value structures
Summary(pl):	Boulder - API dla hierarchicznych struktur znacznik/warto¶æ
Name:		perl-Boulder
Version:	1.30
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Boulder/Boulder-%{version}.tar.gz
# Source0-md5:	87b37e890c959d4ab567614263d64953
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DB_File
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boulder provides a simple stream-oriented format for transmitting data
objects between one or more processes.  It does not provide for the
serialization of Perl objects the way FreezeThaw or Data::Dumper do,
but it does provide the advantage of being language independent.

%description -l pl
Boulder udostêpnia prosty strumieniowy format do transmisji danych
obiektowych pomiêdzy jednym lub wieloma procesami. Nie zapewnia on
serializacji obiektów Perla w taki sposób, jak czyni± to FreezeThaw
lub Data::Dumper, lecz jego zalet± jest niezale¿no¶æ od jêzyka.

%prep
%setup -q -n Boulder-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Stone.pm
%{perl_vendorlib}/Stone
%dir %{perl_vendorlib}/Boulder
%{perl_vendorlib}/Boulder/[^L]*
# Labbase.pm is incomplete and unusable in version 1.27
#%%{perl_vendorlib}/Boulder/L*
%{_mandir}/man3/*
