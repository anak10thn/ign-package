Summary:	IGOS Nusantara Control Panel module ign-cpanel-cinnamon
Name:		ign-cpanel-cinnamon
Version:	1.0.1
Release:	12.2.8
License:	GPLv2
Group:		System Environment/Base
URL:		http://igos-nusantara.or.id
Source0:	%{name}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	ign-cpanel

%description
IGN CPANEL is a control panel for distribution for IGN GNU/Linux, which serves to manage
service, repository, packages, kernel modules, etc.. ign control panel made ​​with PHP-GTK2.

%prep
%setup -q -n %{name}

%install
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir 
/usr/share/ign-cpanel/modules/ign-cpanel-cinnamon
%config %attr(0755,root,root) /usr/share/ign-cpanel/modules/ign-cpanel-cinnamon/*

%changelog
* Wed Feb 9 2012 Ibnu Yahya <ibnu.yahya@toroo.org>
- build module
