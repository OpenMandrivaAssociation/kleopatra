#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Name:		plasma6-kleopatra
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kleopatra/-/archive/%{gitbranch}/kleopatra-%{gitbranchd}.tar.bz2#/kleopatra-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kleopatra-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6MimeTreeParserCore)
BuildRequires:	cmake(KPim6MimeTreeParserWidgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libassuan)
BuildRequires:	pkgconfig(shared-mime-info)
Obsoletes:	%{name}-handbook < 3:16.08.3-1
Requires:	pinentry-qt6
Requires:	plasma6-ksshaskpass

%description
Certificate manager and GUI for OpenPGP and CMS cryptography.

%files -f all.lang
%{_datadir}/applications/org.kde.kwatchgnupg.desktop
%{_datadir}/mime/packages/kleopatra-mime.xml
%{_datadir}/qlogging-categories6/kleopatra.categories
%{_datadir}/qlogging-categories6/kleopatra.renamecategories
%{_bindir}/kleopatra
%{_bindir}/kwatchgnupg
%{_qtdir}/plugins/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfolders.desktop
%{_datadir}/mime/packages/application-vnd-kde-kleopatra.xml
%{_datadir}/metainfo/org.kde.kleopatra.appdata.xml
%{_datadir}/applications/kleopatra_import.desktop
%{_datadir}/applications/org.kde.kleopatra.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/kleopatra
%{_datadir}/kwatchgnupg
%doc %{_docdir}/HTML/*/kleopatra
%doc %{_docdir}/HTML/*/kwatchgnupg
%{_libdir}/libkleopatraclientcore.so.*
%{_libdir}/libkleopatraclientgui.so.*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n kleopatra-%{?git:%{gitbranchd}}%{!?git:%{version}}
# FIXME workaround for compile time error with clang
# src/accessibility/accessiblevaluelabel.cpp:21:48: error: integer value 65536 is outside the valid range of values [0, 65535] for the enumeration type 'Role' [-Wenum-constexpr-conversion]
export CC=gcc
export CXX=g++
export LD=g++
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kleopatra
%find_lang kwatchgnupg

cat *.lang >all.lang
