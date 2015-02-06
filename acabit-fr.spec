%define base_name	acabit
%define name		%{base_name}-fr
%define version		4.3
%define release		9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	Automatic Corpus-based Acquisition of Binary Terms
License:	GPL
Group:		Sciences/Computer science
Source0:	http://www.sciences.univ-nantes.fr/info/perso/permanents/daille/%{base_name}_fr_v%{version}.tar.bz2
Url:		http://www.sciences.univ-nantes.fr/info/perso/permanents/daille/acabit.html
Buildroot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch
Obsoletes:	%{base_name}
provides:	%{base_name}
Requires:	locales-fr

%description
ACABIT is a terminological aquisition software, taking an annotated  text as
input, and returning an ordered list of candidates terms.

This is the french version.

%prep
%setup -q -n %{base_name}_fr_03112004

%build
perl -pi -e 's|require \("lib/(.*)"\);|require ("%{_datadir}/%{name}/$1");|' */*.pl

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 *.pl %{buildroot}%{_bindir}
install -m 644 lib/* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README_FR exemple_fr.txt
%{_bindir}/*
%{_datadir}/%{name}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1:4.3-8mdv2011.0
+ Revision: 616499
- the mass rebuild of 2010.0 packages

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1:4.3-6mdv2010.0
+ Revision: 423861
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1:4.3-5mdv2009.0
+ Revision: 240409
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.3-3mdv2008.0
+ Revision: 67053
- rebuild
- import acabit-fr


* Mon Jun 26 2006 Lenny Cartier <lenny@mandriva.com> 1:4.3-2mdv2007.0
- requires locales-fr

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.3-1mdk 
- new version
- split package in two distinct ones, as english and french version have different versions

* Fri Jul 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 26112003-2mdk 
- fixed spec perms

* Tue Jun 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 26112003-1mdk 
- first mdk release
