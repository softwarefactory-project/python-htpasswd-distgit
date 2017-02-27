%global         commit0 ef677a5af097e3720d0d4c113564edd04de25f97
%global         shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global         checkout 02712017git%{shortcommit0}
%global         sum Library for working with htpasswd user (only basic authorization) and group files
%global         uname htpasswd

Name:           python-htpasswd
Version:        0.1
Release:        1%{checkout}%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/thesharp/%{uname}
Source0:        https://github.com/thesharp/%{uname}/archive/%{commit0}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python2-future

%description
Library for working with htpasswd user (only basic authorization) and group files

%package -n python2-htpasswd

Summary:        %sum
Requires:       python2-future

%description -n python2-htpasswd
Library for working with htpasswd user (only basic authorization) and group files

%prep
%autosetup -n %{uname}-%{commit0}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v

%files -n python2-htpasswd
%{python2_sitelib}/*

%changelog
* Mon Feb 27 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-102272017gitef677a5a
- Initial packaging
