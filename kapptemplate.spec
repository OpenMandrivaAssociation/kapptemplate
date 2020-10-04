Summary:	Templates for KDE Application Development
Name:		kapptemplate
Version:	20.08.1
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Test)
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

#----------------------------------------------------------------------------

%prep
%setup -q

#sed -i -e "s/tar/gtar/g" cmake/modules/KAppTemplateMacro.cmake

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kapptemplate --with-html
