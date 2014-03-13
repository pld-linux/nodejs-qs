%define		pkg	qs
Summary:	Querystring parser
Name:		nodejs-%{pkg}
Version:	0.6.6
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	ec114f32f65c4c9ea24f533b8881a2d7
URL:		https://github.com/visionmedia/node-querystring
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Query string parser for node and the browser supporting nesting, as it
was removed from 0.3.x, so this library provides the previous and
commonly desired behaviour (and twice as fast).

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md
%{nodejs_libdir}/%{pkg}
