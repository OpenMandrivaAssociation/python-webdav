%define pyname	PyWebDAV

Name:		python-webdav
Summary:	Python WebDAV library
Version:	0.9.8
Release:	2
License:	GPLv2
Group:		Development/Python
URL:		https://code.google.com/p/pywebdav/
Source0:	http://pywebdav.googlecode.com/files/%{pyname}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Python WebDAV implementation (level 1 and 2) that features a library
that enables you to integrate WebDAV server capabilities to your application.

%prep
%setup -q -n %{pyname}-%{version}

%build

%install
PYTHONNDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%{_bindir}/davserver
%{py_sitedir}/*
%doc README


%changelog
* Sat Apr 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.8-1
+ Revision: 794282
- imported package python-webdav

