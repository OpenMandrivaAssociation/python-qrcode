%global oname qrcode

Summary:	Python QR Code image generator
Name:		python-%{oname}
Version:	5.2.2
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
%{python_sitelib}/%{oname}/tests
#----------------------------------------------------------------------------

%package -n python2-qrcode
Summary:        Python QR Code image generator
Group:          Development/Python

%description -n python2-qrcode
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes.

%files -n python2-qrcode
%{python2_sitelib}/%{oname}/image/svg.py*
%{python2_sitelib}/%{oname}/image/pil.py

%package -n python2-qrcode-core
Summary:        Python QR Code image generator (core library)
Group:          Development/Python
Requires:       python2-six

%description -n python2-qrcode-core
Core Python module for QR code generation. Does not contain image rendering.

%files -n python2-qrcode-core
%doc LICENSE README.rst CHANGES.rst
%dir %{python2_sitelib}/%{oname}/
%dir %{python2_sitelib}/%{oname}/image
%{python2_sitelib}/%{oname}*.egg-info
%{python2_sitelib}/%{oname}/*.py*
%{python2_sitelib}/%{oname}/image/__init__.py*
%{python2_sitelib}/%{oname}/image/base.py*
%{python2_sitelib}/%{oname}/tests


%prep
%setup -qn %{oname}-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

cp -a . %py2dir

%build
pushd %py2dir
python2 setup.py build
popd

python setup.py build

%install
pushd %py2dir
python2 setup.py install -O1 --skip-build --root %{buildroot}
popd

python setup.py install -O1 --skip-build --root %{buildroot}

