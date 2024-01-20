%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Name:		plasma6-kleopatra
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kleopatra-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6MimeTreeParserWidgets)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libassuan)
BuildRequires:	pkgconfig(shared-mime-info)
Obsoletes:	%{name}-handbook < 3:16.08.3-1
Requires:	pinentry-qt6
Requires:	ksshaskpass

%description
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -f all.lang
%{_datadir}/qlogging-categories6/kleopatra.categories
%{_datadir}/qlogging-categories6/kleopatra.renamecategories
%{_bindir}/kleopatra
%{_bindir}/kwatchgnupg
%{_qt6_plugindir}/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfolders.desktop
%{_datadir}/mime/packages/application-vnd-kde-kleopatra.xml
%{_datadir}/metainfo/org.kde.kleopatra.appdata.xml
%{_datadir}/applications/kleopatra_import.desktop
%{_datadir}/applications/org.kde.kleopatra.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/kconf_update/*
%{_datadir}/kleopatra
%{_datadir}/kwatchgnupg
%doc %{_docdir}/HTML/*/kleopatra
%doc %{_docdir}/HTML/*/kwatchgnupg

#--------------------------------------------------------------------

%define kleopatraclientcore_major 1
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Group:		System/Libraries
Obsoletes:	%{mklibname kf6kleopatraclientcore 1} < 3:17.04.0

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
Obsoletes:	%{mklibname kf6kleopatraclientgui 1} < 3:17.04.0

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
Obsoletes:	%{mklibname kf6libkleopatra -d} < 3:17.04.0

%description -n %{libkleopatra_devel}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{libkleopatra_devel}
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n kleopatra-%{version}
# FIXME differences in interpreting C++20 changes result in
# an incompatibility between clang and libstdc++ parts used
# in kleopatra, resulting in a build failure.
#export CC=gcc
#export CXX=g++
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
%find_lang kwatchgnupg

cat *.lang >all.lang
