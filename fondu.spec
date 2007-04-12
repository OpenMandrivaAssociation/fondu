%define name		fondu
%define fonduversion	051011
%define mdkrelease	%mkrel 1

Name:        fondu
Version:     2.0
Release:     0.%{fonduversion}.%{mdkrelease}
Summary:     Converts between mac and unix fonts
License:     BSD
Group:       Publishing
Source0:     http://fondu.sourceforge.net/fondu_src-%{fonduversion}.tar.bz2
#Patch0:	     fondu-%{fonduversion}-opt.patch.bz2
Url:         http://fondu.sourceforge.net/
BuildRoot:   %{_tmppath}/%{name}-%{version}-root

%description 
Fondu allows you to convert a mac font into a unix one. ufond converts
a unix font into a mac one.

%prep
%setup -n fondu
#%patch0 -p1 -b .opt

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


