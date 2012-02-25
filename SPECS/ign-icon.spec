Summary:IGOS Nusantara ICON THEMES
Name:ign-icon
Version:7.1
Release:12.2.26
License:GPLv2
Group:System Environment/Base
URL:http://igos-nusantara.or.id
Source0:%{name}.tar.gz
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:noarch
Requires:gnome-session

%description
IGN ICON THEMES

%prep
%setup -q -n %{name}

%install
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir 
/usr/share/
%config %attr(0755,root,root) /usr/share/*

%changelog
* Wed Feb 9 2012 Ibnu Yahya <ibnu.yahya@toroo.org>
- build package
