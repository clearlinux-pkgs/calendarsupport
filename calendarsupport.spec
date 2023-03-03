#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : calendarsupport
Version  : 22.12.3
Release  : 54
URL      : https://download.kde.org/stable/release-service/22.12.3/src/calendarsupport-22.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.3/src/calendarsupport-22.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.3/src/calendarsupport-22.12.3.tar.xz.sig
Summary  : Calendar support library
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0
Requires: calendarsupport-data = %{version}-%{release}
Requires: calendarsupport-lib = %{version}-%{release}
Requires: calendarsupport-license = %{version}-%{release}
Requires: calendarsupport-locales = %{version}-%{release}
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-notes-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcontacts-dev
BuildRequires : kguiaddons-dev
BuildRequires : kholidays-dev
BuildRequires : ki18n-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kio-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : pimcommon-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n calendarsupport-22.12.3
cd %{_builddir}/calendarsupport-22.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677805439
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1677805439
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/calendarsupport
cp %{_builddir}/calendarsupport-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/calendarsupport/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/calendarsupport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/calendarsupport/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/calendarsupport/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/calendarsupport/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/calendarsupport/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/calendarsupport/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/calendarsupport/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/calendarsupport-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/calendarsupport/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/calendarsupport-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/calendarsupport/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/calendarsupport-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/calendarsupport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang calendarsupport

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/calendarsupport.categories
/usr/share/qlogging-categories5/calendarsupport.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/CalendarSupport/CalendarSupport/ArchiveDialog
/usr/include/KF5/CalendarSupport/CalendarSupport/CalPrintDefaultPlugins
/usr/include/KF5/CalendarSupport/CalendarSupport/CalPrintPluginBase
/usr/include/KF5/CalendarSupport/CalendarSupport/CalPrinter
/usr/include/KF5/CalendarSupport/CalendarSupport/CalendarSingleton
/usr/include/KF5/CalendarSupport/CalendarSupport/CategoryHierarchyReader
/usr/include/KF5/CalendarSupport/CalendarSupport/CellItem
/usr/include/KF5/CalendarSupport/CalendarSupport/CollectionSelection
/usr/include/KF5/CalendarSupport/CalendarSupport/EventArchiver
/usr/include/KF5/CalendarSupport/CalendarSupport/FreeBusyCalendar
/usr/include/KF5/CalendarSupport/CalendarSupport/FreeBusyItem
/usr/include/KF5/CalendarSupport/CalendarSupport/FreeBusyItemModel
/usr/include/KF5/CalendarSupport/CalendarSupport/FreePeriodModel
/usr/include/KF5/CalendarSupport/CalendarSupport/IdentityManager
/usr/include/KF5/CalendarSupport/CalendarSupport/IncidenceViewer
/usr/include/KF5/CalendarSupport/CalendarSupport/KCalPrefs
/usr/include/KF5/CalendarSupport/CalendarSupport/MessageWidget
/usr/include/KF5/CalendarSupport/CalendarSupport/NoteEditDialog
/usr/include/KF5/CalendarSupport/CalendarSupport/PrintPlugin
/usr/include/KF5/CalendarSupport/CalendarSupport/UriHandler
/usr/include/KF5/CalendarSupport/CalendarSupport/Utils
/usr/include/KF5/CalendarSupport/calendarsupport/archivedialog.h
/usr/include/KF5/CalendarSupport/calendarsupport/calendarsingleton.h
/usr/include/KF5/CalendarSupport/calendarsupport/calendarsupport_export.h
/usr/include/KF5/CalendarSupport/calendarsupport/calprintdefaultplugins.h
/usr/include/KF5/CalendarSupport/calendarsupport/calprinter.h
/usr/include/KF5/CalendarSupport/calendarsupport/calprintpluginbase.h
/usr/include/KF5/CalendarSupport/calendarsupport/categoryhierarchyreader.h
/usr/include/KF5/CalendarSupport/calendarsupport/cellitem.h
/usr/include/KF5/CalendarSupport/calendarsupport/collectionselection.h
/usr/include/KF5/CalendarSupport/calendarsupport/eventarchiver.h
/usr/include/KF5/CalendarSupport/calendarsupport/freebusycalendar.h
/usr/include/KF5/CalendarSupport/calendarsupport/freebusyitem.h
/usr/include/KF5/CalendarSupport/calendarsupport/freebusyitemmodel.h
/usr/include/KF5/CalendarSupport/calendarsupport/freeperiodmodel.h
/usr/include/KF5/CalendarSupport/calendarsupport/identitymanager.h
/usr/include/KF5/CalendarSupport/calendarsupport/incidenceviewer.h
/usr/include/KF5/CalendarSupport/calendarsupport/kcalprefs.h
/usr/include/KF5/CalendarSupport/calendarsupport/kcalprefs_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/messagewidget.h
/usr/include/KF5/CalendarSupport/calendarsupport/noteeditdialog.h
/usr/include/KF5/CalendarSupport/calendarsupport/printplugin.h
/usr/include/KF5/CalendarSupport/calendarsupport/ui_calprintdayconfig_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/ui_calprintincidenceconfig_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/ui_calprintmonthconfig_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/ui_calprinttodoconfig_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/ui_calprintweekconfig_base.h
/usr/include/KF5/CalendarSupport/calendarsupport/urihandler.h
/usr/include/KF5/CalendarSupport/calendarsupport/utils.h
/usr/include/KF5/CalendarSupport/calendarsupport_version.h
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportConfig.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarSupport/KF5CalendarSupportTargets.cmake
/usr/lib64/libKF5CalendarSupport.so
/usr/lib64/qt5/mkspecs/modules/qt_CalendarSupport.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CalendarSupport.so.5
/usr/lib64/libKF5CalendarSupport.so.5.22.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/calendarsupport/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/calendarsupport/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/calendarsupport/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/calendarsupport/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/calendarsupport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/calendarsupport/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/calendarsupport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/calendarsupport/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/calendarsupport/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/calendarsupport/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f calendarsupport.lang
%defattr(-,root,root,-)

