%define name		fondu
%define fonduversion	060102
%define mdkrelease	%mkrel 4

Name:		fondu
Version:	2.0
Release:	0.%{fonduversion}.%{mdkrelease}
Summary:	Converts between mac and unix fonts
License:	BSD
Group:		Publishing
Source0:	http://fondu.sourceforge.net/fondu_src-%{fonduversion}.tar.bz2
Url:		https://fondu.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts:	dgen-sdl

%description 
Fondu allows you to convert a mac font into a unix one. ufond converts
a unix font into a mac one.

%prep
%setup -q -n fondu-%{fonduversion}

%build
%configure2_5x
%make OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_mandir}/man1
%makeinstall
install -m 644 *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/fondu
%{_bindir}/ufond
%{_bindir}/showfond
%{_bindir}/dfont2res
%{_bindir}/frombin
%{_bindir}/tobin
%{_bindir}/lumper
%{_bindir}/setfondname
%{_mandir}/man1/*




%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-0.060102.4mdv2009.0
+ Revision: 245249
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0-0.060102.2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 29 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.060102.2mdv2008.0
+ Revision: 32600
- Release 060102
- Fixed bug #19051.


* Sat Feb 24 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.051011.1mdv2007.0
+ Revision: 125385
- Release: 20051011 cvs.
- Import fondu

* Thu Mar 17 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.0-0.041222.1mdk
- from Emmanuel Andry <eandry@free.fr> : 
	- New version
	- Dropped patch 0

