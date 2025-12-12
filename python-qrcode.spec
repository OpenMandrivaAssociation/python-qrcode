Summary:	Python QR Code image generator
Name:		python-qrcode
Version:	7.4.2
Release:	3
License:	BSD
URL:		https://github.com/lincolnloop/python-qrcode
Source0:	https://pypi.python.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	python%{pyver}dist(pillow)
Requires:	%{name}-core = %{version}-%{release}

#Provides:	python3-qrcode = %{version}-%{release}
Obsoletes:	python3-qrcode-core < %{version}

%description
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes.

%files
%{_bindir}/qr
%{_bindir}/qrcode
%{_mandir}/man1/qr.1*
%{python3_sitelib}/qrcode/image/svg.py*
%{python3_sitelib}/qrcode/image/pil.py*
%{python3_sitelib}/qrcode/image/styledpil.py*
#%%{python3_sitelib}/qrcode/image/__pycache__/svg.*
#%%{python3_sitelib}/qrcode/image/__pycache__/pil.*

#---------------------------------------------------------------------------

%package -n %{name}-core
Summary:	Python 3 QR Code image generator (core library)
Requires:	python-six

%description -n %{name}-core
Core Python module for QR code generation. Does not contain image rendering.

%files -n %{name}-core
%license LICENSE
%doc README.rst CHANGES.rst
%dir %{python3_sitelib}/qrcode/
%dir %{python3_sitelib}/qrcode/image
%dir %{python3_sitelib}/qrcode/image/__pycache__
%{python3_sitelib}/qrcode*.*-info
%{python3_sitelib}/qrcode/*.py*
%{python3_sitelib}/qrcode/__pycache__
%{python3_sitelib}/qrcode/compat/__init__.py*
%{python3_sitelib}/qrcode/compat/etree.py
%{python3_sitelib}/qrcode/compat/pil.py
%{python3_sitelib}/qrcode/compat/__pycache__/__init__.*
%{python3_sitelib}/qrcode/compat/__pycache__/etree.*
%{python3_sitelib}/qrcode/compat/__pycache__/pil.*
%{python3_sitelib}/qrcode/image/__init__.py*
%{python3_sitelib}/qrcode/image/base.py*
%{python3_sitelib}/qrcode/image/styles/
%{python3_sitelib}/qrcode/image/__pycache__/__init__.*
%{python3_sitelib}/qrcode/image/__pycache__/base.*
%{python3_sitelib}/qrcode/image/__pycache__/pil.*
%{python3_sitelib}/qrcode/image/__pycache__/styledpil.*
%{python3_sitelib}/qrcode/image/__pycache__/svg.*

#---------------------------------------------------------------------------

%prep
%autosetup -n qrcode-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

# Remove shebang
sed -i '1d' qrcode/console_scripts.py

%build
%py_build

%install
%py_install

# Do not install tests
rm -r %{buildroot}%{python3_sitelib}/qrcode/tests

#
# In previous iterations of the package, the qr script had been
# renamed to qrcode. This was an unnecessary change from upstream.
#
# We cary this symlink to maintain compat with old packages.
#
ln -s qr %{buildroot}%{_bindir}/qrcode

