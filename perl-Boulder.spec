%include	/usr/lib/rpm/macros.perl
Summary:	Boulder perl module
Summary(pl):	Modu³ perla Boulder
Name:		perl-Boulder
Version:	1.24
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Boulder/Boulder-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
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

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Stone.pm
%{perl_sitelib}/Stone
%{perl_sitelib}/Boulder
%{_mandir}/man3/*
