%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Name:		kleopatra
Version:	19.07.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	boost-devel
BuildRequires:	libassuan-devel
Obsoletes:	%{name}-handbook < 3:16.08.3-1

%description
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -f all.lang
%{_datadir}/qlogging-categories5/kleopatra.categories
%{_datadir}/qlogging-categories5/kleopatra.renamecategories
%{_bindir}/kleopatra
%{_bindir}/kwatchgnupg
%{_qt5_plugindir}/kcm_kleopatra.so
%{_datadir}/metainfo/org.kde.kleopatra.appdata.xml
%{_datadir}/applications/kleopatra_import.desktop
%{_datadir}/applications/org.kde.kleopatra.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/kconf_update/*
%{_datadir}/kleopatra
%{_datadir}/kservices5/*.desktop
%{_datadir}/kwatchgnupg
%{_docdir}/HTML/*/kleopatra
%{_docdir}/HTML/*/kwatchgnupg

#--------------------------------------------------------------------

%define kleopatraclientcore_major 1
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Group:		System/Libraries
Obsoletes:	%{mklibname kf5kleopatraclientcore 1} < 3:17.04.0

%description -n %{libkleopatraclientcore}
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -n %{libkleopatraclientcore}
%_libdir/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#--------------------------------------------------------------------

%define kleopatraclientgui_major 1
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %{libkleopatraclientgui}
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Group:		System/Libraries
Obsoletes:	%{mklibname kf5kleopatraclientgui 1} < 3:17.04.0

%description -n %{libkleopatraclientgui}
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -n %{libkleopatraclientgui}
%{_libdir}/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#--------------------------------------------------------------------

%define libkleopatra_devel %mklibname libkleopatra -d

%package -n %{libkleopatra_devel}

Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkleopatraclientcore} = %{EVRD}
Requires:	%{libkleopatraclientgui} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kf5libkleopatra -d} < 3:17.04.0

%description -n %{libkleopatra_devel}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{libkleopatra_devel}
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
%find_lang kwatchgnupg

cat *.lang >all.lang
