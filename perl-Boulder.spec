%include	/usr/lib/rpm/macros.perl
Summary:	Boulder perl module
Summary(pl):	Modu³ perla Boulder
Name:		perl-Boulder
Version:	1.30
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Boulder/Boulder-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boulder - Read and write tag/value data from an input stream.

%description -l pl
Modu³ perla Boulder.

%prep
%setup -q -n Boulder-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%{perl_vendorlib}/Boulder.pod
%{_mandir}/man3/*
