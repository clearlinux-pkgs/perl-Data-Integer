#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Integer
Version  : 0.006
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Integer-0.006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Integer-0.006.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-integer-perl/libdata-integer-perl_0.006-1.debian.tar.xz
Summary  : 'details of the native integer data type'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Integer-license = %{version}-%{release}
Requires: perl-Data-Integer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build)

%description
NAME
Data::Integer - details of the native integer data type
DESCRIPTION
This module is about the native integer numerical data type.  A native
integer is one of the types of datum that can appear in the numeric part
of a Perl scalar.  This module supplies constants describing the native
integer type.

%package dev
Summary: dev components for the perl-Data-Integer package.
Group: Development
Provides: perl-Data-Integer-devel = %{version}-%{release}
Requires: perl-Data-Integer = %{version}-%{release}

%description dev
dev components for the perl-Data-Integer package.


%package license
Summary: license components for the perl-Data-Integer package.
Group: Default

%description license
license components for the perl-Data-Integer package.


%package perl
Summary: perl components for the perl-Data-Integer package.
Group: Default
Requires: perl-Data-Integer = %{version}-%{release}

%description perl
perl components for the perl-Data-Integer package.


%prep
%setup -q -n Data-Integer-0.006
cd %{_builddir}
tar xf %{_sourcedir}/libdata-integer-perl_0.006-1.debian.tar.xz
cd %{_builddir}/Data-Integer-0.006
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Integer-0.006/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Integer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Integer/c6109303374e4f9043f469c6a736c11ab30dc38b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Integer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Integer/c6109303374e4f9043f469c6a736c11ab30dc38b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
