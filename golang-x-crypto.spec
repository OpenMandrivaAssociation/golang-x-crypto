# Run tests in check section
%bcond_with check

# https://github.com/golang/crypto
%global goipath		golang.org/x/crypto
%global forgeurl	https://github.com/golang/crypto
Version:		0.28.0

%gometa

Summary:	Go supplementary cryptography libraries
Name:		golang-x-crypto

Release:	1
Source0:	https://github.com/golang/crypto/archive/v%{version}/crypto-%{version}.tar.gz
URL:		https://github.com/golang/crypto
License:	BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(golang.org/x/net/idna)
BuildRequires:	golang(golang.org/x/sys/cpu)
BuildRequires:	golang(golang.org/x/term)
BuildArch:	noarch

%description
This package provides supplementary Go cryptography libraries.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n crypto-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

