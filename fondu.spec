%define name		fondu
%define fonduversion	060102
%define mdkrelease	%mkrel 2

Name:		fondu
Version:	2.0
Release:	0.%{fonduversion}.%{mdkrelease}
Summary:	Converts between mac and unix fonts
License:	BSD
Group:		Publishing
Source0:	http://fondu.sourceforge.net/fondu_src-%{fonduversion}.tar.bz2
Url:		http://fondu.sourceforge.net/
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


