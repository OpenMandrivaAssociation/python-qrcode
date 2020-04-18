%global pkgname qrcode

Name:           python-%{pkgname}
Version:        6.1
Release:        5%{?dist}
Summary:        Python QR Code image generator

License:        BSD
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        https://pypi.python.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-imaging
BuildRequires:  python-six

%global _description\
This module uses the Python Imaging Library (PIL) to allow for the\
generation of QR Codes.

%description %_description

%package -n python3-%{pkgname}
Summary:        Python QR Code image generator
Requires:       python-imaging
# For entry point:
Requires:       python3-setuptools
Requires:       python3-%{pkgname}-core = %{version}-%{release}

%description -n python3-%{pkgname}
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes. Python 3 version.

%package -n python3-%{pkgname}-core
Requires:       python-six
Summary:        Python 3 QR Code image generator (core library)

%description -n python3-%{pkgname}-core
Core Python 3 module for QR code generation. Does not contain image rendering.

%prep
%autosetup -n qrcode-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

# Remove shebang
sed -i '1d' qrcode/console_scripts.py

%build
%py3_build

%install
%py3_install

# Do not install tests
rm -r %{buildroot}%{python3_sitelib}/%{pkgname}/tests

#
# In previous iterations of the package, the qr script had been
# renamed to qrcode. This was an unnecessary change from upstream.
#
# We cary this symlink to maintain compat with old packages.
#
ln -s qr %{buildroot}%{_bindir}/qrcode

%files -n python3-%{pkgname}
%{_bindir}/qr
%{_bindir}/qrcode
%{_mandir}/man1/qr.1*
%{python3_sitelib}/%{pkgname}/image/svg.py*
%{python3_sitelib}/%{pkgname}/image/pil.py*
%{python3_sitelib}/%{pkgname}/image/__pycache__/svg.*
%{python3_sitelib}/%{pkgname}/image/__pycache__/pil.*

%files -n python3-%{pkgname}-core
%doc README.rst CHANGES.rst
%license LICENSE
%dir %{python3_sitelib}/%{pkgname}/
%dir %{python3_sitelib}/%{pkgname}/image
%dir %{python3_sitelib}/%{pkgname}/image/__pycache__
%{python3_sitelib}/%{pkgname}*.egg-info
%{python3_sitelib}/%{pkgname}/*.py*
%{python3_sitelib}/%{pkgname}/__pycache__
%{python3_sitelib}/%{pkgname}/image/__init__.py*
%{python3_sitelib}/%{pkgname}/image/base.py*
%{python3_sitelib}/%{pkgname}/image/__pycache__/__init__.*
%{python3_sitelib}/%{pkgname}/image/__pycache__/base.*
