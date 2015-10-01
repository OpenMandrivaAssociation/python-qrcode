%global oname qrcode

Summary:	Python QR Code image generator
Name:		python-%{oname}
Version:	5.0.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://github.com/lincolnloop/python-qrcode
Source0:	http://pypi.python.org/packages/source/q/qrcode/%{oname}-%{version}.tar.gz
BuildRequires:	python-imaging
BuildRequires:	python-setuptools
BuildRequires:	python-six
BuildRequires:	pkgconfig(python)
Requires:	python-imaging
Requires:	%{name}-core = %{EVRD}
BuildArch:	noarch

%description
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes.

%files
%{_bindir}/qr
%{_mandir}/man1/qr.1*
%{python_sitelib}/%{oname}/image/svg.py*
%{python_sitelib}/%{oname}/image/pil.py*

#----------------------------------------------------------------------------

%package core
Summary:	Python QR Code image generator (core library)
Group:		Development/Python
Requires:	python-six

%description core
Core Python module for QR code generation. Does not contain image rendering.

%files core
%doc LICENSE README.rst CHANGES.rst
%dir %{python_sitelib}/%{oname}/
%dir %{python_sitelib}/%{oname}/image
%{python_sitelib}/%{oname}*.egg-info
%{python_sitelib}/%{oname}/*.py*
%{python_sitelib}/%{oname}/image/__init__.py*
%{python_sitelib}/%{oname}/image/base.py*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

