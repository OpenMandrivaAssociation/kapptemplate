#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Templates for KDE Application Development
Name:		plasma6-kapptemplate
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kapptemplate/-/archive/%{gitbranch}/kapptemplate-%{gitbranchd}.tar.bz2#/kapptemplate-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kapptemplate-%{version}.tar.xz
%endif
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Quick)
#BuildRequires:	gnutar

%description
KAppTemplate is a set of modular shell scripts that will create a framework for
any number of KDE application types. At its base level, it handles creation of
things like the automake/autoconf framework, lsm files, RPM spec files, and po
files. Then, there are individual modules that allow you to create a skeleton
KDE application, a KPart application, a KPart plugin, or even convert existing
source code to the KDE framework.

%files -f kapptemplate.lang
%{_bindir}/kapptemplate
%{_datadir}/metainfo/org.kde.kapptemplate.appdata.xml
%{_datadir}/applications/org.kde.kapptemplate.desktop
%{_datadir}/config.kcfg/kapptemplate.kcfg
%{_iconsdir}/hicolor/*/apps/*.*g
%{_datadir}/kdevappwizard/templates/*.tar.*
%{_datadir}/qlogging-categories6/kapptemplate.categories

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kapptemplate-%{?git:%{gitbranchd}}%{!?git:%{version}}

#sed -i -e "s/tar/gtar/g" cmake/modules/KAppTemplateMacro.cmake

%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kapptemplate --with-html
