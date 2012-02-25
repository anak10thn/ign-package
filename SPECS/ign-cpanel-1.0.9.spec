Summary:IGOS Nusantara Control Panel
Name:ign-cpanel
Version:1.0.9
Release:12.2.25
License:GPLv2
Group:System Environment/Base
URL:http://igos-nusantara.or.id
Source0:%{name}-%{version}.tar.gz
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:noarch
Requires:php-cairo
Requires:php-cli
Requires:php-gtk2
Requires:php-process

%description
IGN CPANEL is a control panel for distribution for IGN GNU/Linux, which serves to manage
service, repository, packages, kernel modules, etc.. ign control panel made ​​with PHP-GTK2.

%prep
%setup -q -n %{name}-%{version}

%install
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir 
/usr/share/ign-cpanel/
/usr/sbin/
/usr/share/applications/
%config %attr(0755,root,root) /usr/share/ign-cpanel/*

%changelog
* Sat Feb 25 2012 Ibnu Yahya <ibnu.yahya@toroo.org>
- Edit file conf.php
* Wed Feb 8 2012 Nana Suryana <nana@suryana.web.id>
- fix spec file
* Thu Feb 2 2012 Ibnu Yahya <ibnu.yahya@toroo.org>
- Perbaikan module scanner.
