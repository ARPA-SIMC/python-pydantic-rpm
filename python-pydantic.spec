Name:           python-pydantic
Version:        1.9.2
Release:        1%{?dist}
Summary:        Data validation and settings management using python type hints


License:        MIT
URL:            https://github.com/pydantic/pydantic
Source0:        https://files.pythonhosted.org/packages/fd/8f/3f7e88b507dbdfec8f1f914294aa8831edffb03d668799c65b4b46331c8a/pydantic-1.9.2.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-dataclasses
BuildRequires:  python3-typing-extensions
BuildRequires:  python3-email-validator
BuildRequires:  python3-dotenv

%description
Data validation and settings management using Python type hints.

Fast and extensible, pydantic plays nicely with your linters/IDE/brain. Define
how data should be in pure, canonical Python 3.6+; validate it with pydantic.

%package        -n python3-pydantic
Summary:        Data validation and settings management using python type hints
%{?python_provide:%python_provide python3-pydantic}
Requires:       python3-dataclasses
Requires:       python3-typing-extensions
Requires:       python3-email-validator
Requires:       python3-dotenv

%description    -n python3-pydantic
Data validation and settings management using Python type hints.

Fast and extensible, pydantic plays nicely with your linters/IDE/brain. Define
how data should be in pure, canonical Python 3.6+; validate it with pydantic.

%prep
%autosetup -n pydantic-%{version}

%build
%py3_build

%install
%py3_install

# %check
# %{__python3} setup.py test

%files -n python3-pydantic
%license LICENSE
%doc README.md
%{python3_sitelib}/pydantic
%{python3_sitelib}/pydantic-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Mar 13 2024 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.9.2-1
- Fist release
