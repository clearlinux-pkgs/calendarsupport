#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : calendarsupport
Version  : 19.12.2
Release  : 19
URL      : https://download.kde.org/stable/release-service/19.12.2/src/calendarsupport-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/calendarsupport-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/calendarsupport-19.12.2.tar.xz.sig
Summary  : Calendar support library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: calendarsupport-data = %{version}-%{release}
Requires: calendarsupport-lib = %{version}-%{release}
Requires: calendarsupport-license = %{version}-%{release}
Requires: calendarsupport-locales = %{version}-%{release}
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdepim-apps-libs-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev

%description
calendarsupport/next is the place for clean/documented/unit_tested code that is almost ready to go to kdepimlibs.

%package data
Summary: data components for the calendarsupport package.
Group: Data

%description data
data components for the calendarsupport package.


%package dev
Summary: dev components for the calendarsupport package.
Group: Development
Requires: calendarsupport-lib = %{version}-%{release}
Requires: calendarsupport-data = %{version}-%{release}
Provides: calendarsupport-devel = %{version}-%{release}
Requires: calendarsupport = %{version}-%{release}
Requires: calendarsupport = %{version}-%{release}

%description dev
dev components for the calendarsupport package.


%package lib
Summary: lib components for the calendarsupport package.
Group: Libraries
Requires: calendarsupport-data = %{version}-%{release}
Requires: calendarsupport-license = %{version}-%{release}

%description lib
lib components for the calendarsupport package.


%package license
Summary: license components for the calendarsupport package.
Group: Default

%description license
license components for the calendarsupport package.


%package locales
Summary: locales components for the calendarsupport package.
Group: Default

%description locales
locales components for the calendarsupport package.


%prep
%setup -q -n calendarsupport-19.12.2
cd %{_builddir}/calendarsupport-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581098546
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581098546
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/calendarsupport
cp %{_builddir}/calendarsupport-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/calendarsupport/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/calendarsupport-19.12.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/calendarsupport/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang calendarsupport

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/calendarplugin.desktop
/usr/share/qlogging-categories5/calendarsupport.categories
/usr/share/qlogging-categories5/calendarsupport.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/CalendarSupport/ArchiveDialog
/usr/include/KF5/CalendarSupport/CalPrintDefaultPlugins
/usr/include/KF5/CalendarSupport/CalPrintPluginBase
/usr/include/KF5/CalendarSupport/CalPrinter
/usr/include/KF5/CalendarSupport/CalendarSingleton
/usr/include/KF5/CalendarSupport/CategoryConfig
/usr/include/KF5/CalendarSupport/CategoryHierarchyReader
/usr/include/KF5/CalendarSupport/CellItem
/usr/include/KF5/CalendarSupport/CollectionSelection
/usr/include/KF5/CalendarSupport/EventArchiver
/usr/include/KF5/CalendarSupport/FreeBusyCalendar
/usr/include/KF5/CalendarSupport/FreeBusyItem
/usr/include/KF5/CalendarSupport/FreeBusyItemModel
/usr/include/KF5/CalendarSupport/FreePeriodModel
/usr/include/KF5/CalendarSupport/IdentityManager
/usr/include/KF5/CalendarSupport/IncidenceViewer
/usr/include/KF5/CalendarSupport/KCalPrefs
/usr/include/KF5/CalendarSupport/MessageWidget
/usr/include/KF5/CalendarSupport/Plugin
/usr/include/KF5/CalendarSupport/PrintPlugin
/usr/include/KF5/CalendarSupport/Utils
/usr/include/KF5/calendarsupport/archivedialog.h
/usr/include/KF5/calendarsupport/calendarsingleton.h
/usr/include/KF5/calendarsupport/calendarsupport_export.h
/usr/include/KF5/calendarsupport/calprintdefaultplugins.h
/usr/include/KF5/calendarsupport/calprinter.h
/usr/include/KF5/calendarsupport/calprintpluginbase.h
/usr/include/KF5/calendarsupport/categoryconfig.h
/usr/include/KF5/calendarsupport/categoryhierarchyreader.h
/usr/include/KF5/calendarsupport/cellitem.h
/usr/include/KF5/calendarsupport/collectionselection.h
/usr/include/KF5/calendarsupport/eventarchiver.h
/usr/include/KF5/calendarsupport/freebusycalendar.h
/usr/include/KF5/calendarsupport/freebusyitem.h
/usr/include/KF5/calendarsupport/freebusyitemmodel.h
/usr/include/KF5/calendarsupport/freeperiodmodel.h
/usr/include/KF5/calendarsupport/identitymanager.h
/usr/include/KF5/calendarsupport/incidenceviewer.h
/usr/include/KF5/calendarsupport/kcalprefs.h
/usr/include/KF5/calendarsupport/kcalprefs_base.h
/usr/include/KF5/calendarsupport/messagewidget.h
/usr/include/KF5/calendarsupport/plugin.h
/usr/include/KF5/calendarsupport/printplugin.h
/usr/include/KF5/calendarsupport/ui_calprintdayconfig_base.h
/usr/include/KF5/calendarsupport/ui_calprintincidenceconfig_base.h
/usr/include/KF5/calendarsupport/ui_calprintmonthconfig_base.h
/usr/include/KF5/calendarsupport/ui_calprinttodoconfig_base.h
/usr/include/KF5/calendarsupport/ui_calprintweekconfig_base.h
/usr/include/KF5/calendarsupport/utils.h
/usr/include/KF5/calendarsupport_version.h
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportConfig.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportTargets.cmake
/usr/lib64/libKF5CalendarSupport.so
/usr/lib64/qt5/mkspecs/modules/qt_CalendarSupport.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CalendarSupport.so.5
/usr/lib64/libKF5CalendarSupport.so.5.13.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/calendarsupport/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/calendarsupport/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f calendarsupport.lang
%defattr(-,root,root,-)

