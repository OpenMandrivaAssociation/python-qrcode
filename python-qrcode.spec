%global module qrcode

Summary:	Python QR Code image generator
Name:		python-%{module}
Version:	7.3.1
Release:	1
License:	BSD
URL:		https://github.com/lincolnloop/python-qrcode
Source0:	https://pypi.python.org/packages/source/q/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(six)

Requires:	python-imaging
Requires:	%{name}-core = %{version}-%{release}

Provides:	python3-%{module} = %{version}-%{release}
Obsoletes:	python3-%{module}-core < %{version}

%description
This module uses the Python Imaging Library (PIL) to allow for the\
generation of QR Codes.

%files
%{_bindir}/qr
%{_bindir}/qrcode
%{_mandir}/man1/qr.1*
%{python3_sitelib}/%{module}/image/svg.py*
%{python3_sitelib}/%{module}/image/pil.py*
%{python3_sitelib}/%{module}/image/styledpil.py*
#%%{python3_sitelib}/%{module}/image/__pycache__/svg.*
#%%{python3_sitelib}/%{module}/image/__pycache__/pil.*

#---------------------------------------------------------------------------

%package -n %{name}-core
Summary:	Python 3 QR Code image generator (core library)
Requires:	python-six

%description -n %{name}-core
Core Python 3 module for QR code generation. Does not contain image rendering.

%files -n %{name}-core
%license LICENSE
%doc README.rst CHANGES.rst
%dir %{python3_sitelib}/%{module}/
%dir %{python3_sitelib}/%{module}/image
#%%dir %{python3_sitelib}/%{module}/image/__pycache__
%{python3_sitelib}/%{module}*.egg-info
%{python3_sitelib}/%{module}/*.py*
#%%{python3_sitelib}/%{module}/__pycache__
%{python3_sitelib}/%{module}/image/__init__.py*
%{python3_sitelib}/%{module}/image/base.py*
%{python3_sitelib}/%{module}/image/styles/
#%%{python3_sitelib}/%{module}/image/__pycache__/__init__.*
#%%{python3_sitelib}/%{module}/image/__pycache__/base.*
#%%{python3_sitelib}/%{module}/image/__pycache__/styledpil.*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

# Remove shebang
sed -i '1d' qrcode/console_scripts.py

%build
%py_build

%install
%py_install

# Do not install tests
rm -r %{buildroot}%{python3_sitelib}/%{module}/tests

#
# In previous iterations of the package, the qr script had been
# renamed to qrcode. This was an unnecessary change from upstream.
#
# We cary this symlink to maintain compat with old packages.
#
ln -s qr %{buildroot}%{_bindir}/qrcode

