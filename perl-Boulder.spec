%include	/usr/lib/rpm/macros.perl
Summary:	Boulder perl module
Summary(pl):	Modu³ perla Boulder
Name:		perl-Boulder
Version:	1.30
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Boulder/Boulder-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boulder - Read and write tag/value data from an input stream.

%description -l pl
Modu³ perla Boulder.

%prep
%setup -q -n Boulder-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Stone.pm
%{perl_sitelib}/Stone
%dir %{perl_sitelib}/Boulder
%{perl_sitelib}/Boulder/[^L]*
# Labbase.pm is incomplete and unusable in version 1.27
#%{perl_sitelib}/Boulder/L*
%{perl_sitelib}/Boulder.pod
%{_mandir}/man3/*
