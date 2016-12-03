Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Name:		kleopatra
Version:	16.08.3
Epoch:		3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5DocTools)

# Kdepimlibs packages
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Gpgmepp)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test) 
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	boost-devel
Obsoletes:	%{name}-handbook < 3:16.08.3-1

%description
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files
%{_sysconfdir}/xdg/kleopatra.categories
%{_kde5_bindir}/kleopatra
%{_kde5_bindir}/kwatchgnupg
%{_qt5_plugindir}/kcm_kleopatra.so
%{_kde5_datadir}/metainfo/org.kde.kleopatra.appdata.xml
%{_kde5_datadir}/applications/kleopatra_import.desktop
%{_kde5_datadir}/applications/org.kde.kleopatra.desktop
%{_iconsdir}/*/*/*/*
%{_kde5_datadir}/kconf_update/*
%{_kde5_datadir}/kleopatra
%{_kde5_datadir}/kservices5/*.desktop
%{_kde5_datadir}/kwatchgnupg
%{_kde5_docdir}/HTML/en/kleopatra
%{_kde5_docdir}/HTML/en/kwatchgnupg

#--------------------------------------------------------------------

%define kf5kleopatraclientcore_major 1
%define libkleopatraclientcore %mklibname kf5kleopatraclientcore %{kf5kleopatraclientcore_major}

%package -n %libkleopatraclientcore
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Group:		System/Libraries


%description -n %libkleopatraclientcore
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -n %libkleopatraclientcore
%_kde5_libdir/libkleopatraclientcore.so.%{kf5kleopatraclientcore_major}*

#--------------------------------------------------------------------

%define kf5kleopatraclientgui_major 1
%define libkleopatraclientgui %mklibname kf5kleopatraclientgui %{kf5kleopatraclientgui_major}

%package -n %libkleopatraclientgui
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Group:		System/Libraries


%description -n %libkleopatraclientgui
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -n %libkleopatraclientgui
%_kde5_libdir/libkleopatraclientgui.so.%{kf5kleopatraclientgui_major}*

#--------------------------------------------------------------------

%define kf5libkleopatra_devel %mklibname kf5libkleopatra -d

%package -n %kf5libkleopatra_devel

Summary:	Devel stuff for %name
Group:		Development/KDE and Qt
Requires:	%libkleopatraclientcore = %{EVRD}
Requires:	%libkleopatraclientgui = %{EVRD}
Provides:	%name-devel = %{EVRD}

%description -n %kf5libkleopatra_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf5libkleopatra_devel
%{_kde5_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

#find_lang --all %{name}5

