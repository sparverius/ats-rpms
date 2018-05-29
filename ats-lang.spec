Name:           ats-lang
Version:        3.10
Release:        1%{?dist}
Summary:        Compilers for ATS programming language

License:        GPLv3
URL:            https://www.github.com/%{name}
Source0:        https://www.github.com/%{name}/releases/%{name}-%{version}.tar.gz
                # https://sourceforge.net/projects/ats2-lang/files/ats2-lang/ats2-postiats-0.3.10/ATS2-Postiats-0.3.10.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gmp-devel
BuildRequires:  gc-devel
BuildRequires:  json-c-devel

%description
ats-lang compilers -- patscc patsopt and myatscc

%prep
%setup -q

%configure
./configure

%build
make all

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/bin/patsopt %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/bin/patscc %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/bin/myatscc %{buildroot}%{_bindir}

%files
%doc AUTHORS COPYING VERSION CHANGES-ats2
%license COPYING
%{_bindir}/patsopt
%{_bindir}/patscc
%{_bindir}/myatscc

%changelog
* Tue May 29 2018 root
- First cello package
