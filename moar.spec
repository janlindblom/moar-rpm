Name: moar
Version: 1.23.6
Release: 1%{?dist}

Summary: A pager designed to just do the right thing without any configuration.
License: BSD
BuildArch: x86_64
Source0: https://github.com/walles/moar/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make, git, go
BuildRequires:  golang >= 1.16


%prep
%autosetup -n %{name}-%{version}

%build
export PATH=$PWD/go/bin:$PATH
go version
sh build.sh

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md MOUSE.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Fri March 1 2024 Jan Lindblom <janlindblom@fastmail.fm> - 1.23.6-1
- First moar package
