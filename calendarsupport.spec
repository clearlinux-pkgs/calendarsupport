#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 81e1eeb
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : calendarsupport
Version  : 24.02.2
Release  : 69
URL      : https://download.kde.org/stable/release-service/24.02.2/src/calendarsupport-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/calendarsupport-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/calendarsupport-24.02.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n calendarsupport-24.02.2
cd %{_builddir}/calendarsupport-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712940868
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712940868
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/calendarsupport
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
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang calendarsupport6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/calendarsupport.categories
/usr/share/qlogging-categories6/calendarsupport.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/CalendarSupport/CalendarSupport/ArchiveDialog
/usr/include/KPim6/CalendarSupport/CalendarSupport/CalPrintDefaultPlugins
/usr/include/KPim6/CalendarSupport/CalendarSupport/CalPrintPluginBase
/usr/include/KPim6/CalendarSupport/CalendarSupport/CalPrinter
/usr/include/KPim6/CalendarSupport/CalendarSupport/CalendarSingleton
/usr/include/KPim6/CalendarSupport/CalendarSupport/CategoryHierarchyReader
/usr/include/KPim6/CalendarSupport/CalendarSupport/CellItem
/usr/include/KPim6/CalendarSupport/CalendarSupport/CollectionSelection
/usr/include/KPim6/CalendarSupport/CalendarSupport/EventArchiver
/usr/include/KPim6/CalendarSupport/CalendarSupport/FreeBusyCalendar
/usr/include/KPim6/CalendarSupport/CalendarSupport/FreeBusyItem
/usr/include/KPim6/CalendarSupport/CalendarSupport/FreeBusyItemModel
/usr/include/KPim6/CalendarSupport/CalendarSupport/FreePeriodModel
/usr/include/KPim6/CalendarSupport/CalendarSupport/IdentityManager
/usr/include/KPim6/CalendarSupport/CalendarSupport/IncidenceViewer
/usr/include/KPim6/CalendarSupport/CalendarSupport/KCalPrefs
/usr/include/KPim6/CalendarSupport/CalendarSupport/MessageWidget
/usr/include/KPim6/CalendarSupport/CalendarSupport/NoteEditDialog
/usr/include/KPim6/CalendarSupport/CalendarSupport/PrintPlugin
/usr/include/KPim6/CalendarSupport/CalendarSupport/UriHandler
/usr/include/KPim6/CalendarSupport/CalendarSupport/Utils
/usr/include/KPim6/CalendarSupport/calendarsupport/archivedialog.h
/usr/include/KPim6/CalendarSupport/calendarsupport/calendarsingleton.h
/usr/include/KPim6/CalendarSupport/calendarsupport/calendarsupport_export.h
/usr/include/KPim6/CalendarSupport/calendarsupport/calprintdefaultplugins.h
/usr/include/KPim6/CalendarSupport/calendarsupport/calprinter.h
/usr/include/KPim6/CalendarSupport/calendarsupport/calprintpluginbase.h
/usr/include/KPim6/CalendarSupport/calendarsupport/categoryhierarchyreader.h
/usr/include/KPim6/CalendarSupport/calendarsupport/cellitem.h
/usr/include/KPim6/CalendarSupport/calendarsupport/collectionselection.h
/usr/include/KPim6/CalendarSupport/calendarsupport/eventarchiver.h
/usr/include/KPim6/CalendarSupport/calendarsupport/freebusycalendar.h
/usr/include/KPim6/CalendarSupport/calendarsupport/freebusyitem.h
/usr/include/KPim6/CalendarSupport/calendarsupport/freebusyitemmodel.h
/usr/include/KPim6/CalendarSupport/calendarsupport/freeperiodmodel.h
/usr/include/KPim6/CalendarSupport/calendarsupport/identitymanager.h
/usr/include/KPim6/CalendarSupport/calendarsupport/incidenceviewer.h
/usr/include/KPim6/CalendarSupport/calendarsupport/kcalprefs.h
/usr/include/KPim6/CalendarSupport/calendarsupport/kcalprefs_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/messagewidget.h
/usr/include/KPim6/CalendarSupport/calendarsupport/noteeditdialog.h
/usr/include/KPim6/CalendarSupport/calendarsupport/printplugin.h
/usr/include/KPim6/CalendarSupport/calendarsupport/ui_calprintdayconfig_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/ui_calprintincidenceconfig_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/ui_calprintmonthconfig_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/ui_calprinttodoconfig_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/ui_calprintweekconfig_base.h
/usr/include/KPim6/CalendarSupport/calendarsupport/urihandler.h
/usr/include/KPim6/CalendarSupport/calendarsupport/utils.h
/usr/include/KPim6/CalendarSupport/calendarsupport_version.h
/usr/lib64/cmake/KPim6CalendarSupport/KPim6CalendarSupportConfig.cmake
/usr/lib64/cmake/KPim6CalendarSupport/KPim6CalendarSupportConfigVersion.cmake
/usr/lib64/cmake/KPim6CalendarSupport/KPim6CalendarSupportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6CalendarSupport/KPim6CalendarSupportTargets.cmake
/usr/lib64/libKPim6CalendarSupport.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6CalendarSupport.so.6.0.2
/usr/lib64/libKPim6CalendarSupport.so.6
/usr/lib64/libKPim6CalendarSupport.so.6.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/calendarsupport/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/calendarsupport/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/calendarsupport/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/calendarsupport/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/calendarsupport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/calendarsupport/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/calendarsupport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/calendarsupport/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/calendarsupport/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f calendarsupport6.lang
%defattr(-,root,root,-)

