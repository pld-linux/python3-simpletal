%define 	fname	SimpleTAL
%define		module	%(echo %{fname} | tr A-Z a-z)

Summary:	Stand alone implementation of the TAL, TALES and METAL specifications
Summary(pl.UTF-8):	Niezależna implementacja specyfikacji TAL, TALES i METAL
Name:		python3-simpletal
Version:	5.1
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://www.owlfish.com/software/simpleTAL/downloads/%{fname}-%{version}.tar.gz
# Source0-md5:	2c43fb2376d501c2957bda26c81c419f
URL:		http://www.owlfish.com/software/simpleTAL/
BuildRequires:	python3
%pyrequires_eq	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and
METAL specifications used in Zope to power HTML and XML templates.
SimpleTAL is an independent implementation of TAL; there are no
dependencies on Zope nor is any of the Zope work re-used.

%description -l pl.UTF-8
SimpleTAL to samodzielna implementacja specyfikacji TAL, TALES i METAL
używanych w Zope do wspomagania szablonów HTML i XML. SimpleTAL to
niezależna implementacja TAL; nie zależy od Zope i nie jest ponownym
użyciem żadnej z prac Zope.

%package examples
Summary:	Example files for SimpleTAL
Summary(pl.UTF-8):	Pliki przykładów dla SimpleTAL
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for SimpleTAL. 

%description examples -l pl.UTF-8
Pliki przykładów dla SimpleTAL.

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt README.txt documentation/html
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{fname}-%{version}-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
