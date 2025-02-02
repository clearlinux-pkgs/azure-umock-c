#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: 6a4b23bb3e69
#
Name     : azure-umock-c
Version  : 366cda39ae31a4891a5fbfac32a2961b1aa02e61
Release  : 2
URL      : https://github.com/Azure/umock-c/archive/366cda39ae31a4891a5fbfac32a2961b1aa02e61/azure-umock-c-366cda39ae31a4891a5fbfac32a2961b1aa02e61.tar.gz
Source0  : https://github.com/Azure/umock-c/archive/366cda39ae31a4891a5fbfac32a2961b1aa02e61/azure-umock-c-366cda39ae31a4891a5fbfac32a2961b1aa02e61.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: azure-umock-c-license = %{version}-%{release}
BuildRequires : azure-c-logging-dev
BuildRequires : azure-macro-utils-c-dev
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-broken-cmake.patch
Patch2: 0002-Fix-linking-against-header-only-macro_utils_c.patch

%description
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

%package dev
Summary: dev components for the azure-umock-c package.
Group: Development
Provides: azure-umock-c-devel = %{version}-%{release}
Requires: azure-umock-c = %{version}-%{release}

%description dev
dev components for the azure-umock-c package.


%package license
Summary: license components for the azure-umock-c package.
Group: Default

%description license
license components for the azure-umock-c package.


%prep
%setup -q -n umock-c-366cda39ae31a4891a5fbfac32a2961b1aa02e61
cd %{_builddir}/umock-c-366cda39ae31a4891a5fbfac32a2961b1aa02e61
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726528893
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -Duse_installed_dependencies=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726528893
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-umock-c
cp %{_builddir}/umock-c-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/azure-umock-c/c4770fd76438e6ead5e333d693d65b1b68d924b0 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
# Move the installed header files to a real location
if [[ -d %{buildroot}/umock_c ]]; then
mkdir -p %{buildroot}/usr/include
mv %{buildroot}/umock_c %{buildroot}/usr/include/
fi
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/umock_c/umock_c.h
/usr/include/umock_c/umock_c_internal.h
/usr/include/umock_c/umock_c_negative_tests.h
/usr/include/umock_c/umock_c_prod.h
/usr/include/umock_c/umock_lock_factory.h
/usr/include/umock_c/umock_lock_factory_default.h
/usr/include/umock_c/umock_lock_if.h
/usr/include/umock_c/umock_log.h
/usr/include/umock_c/umockalloc.h
/usr/include/umock_c/umockautoignoreargs.h
/usr/include/umock_c/umockcall.h
/usr/include/umock_c/umockcallpairs.h
/usr/include/umock_c/umockcallrecorder.h
/usr/include/umock_c/umockstring.h
/usr/include/umock_c/umocktypename.h
/usr/include/umock_c/umocktypes.h
/usr/include/umock_c/umocktypes_bool.h
/usr/include/umock_c/umocktypes_c.h
/usr/include/umock_c/umocktypes_charptr.h
/usr/include/umock_c/umocktypes_stdint.h
/usr/include/umock_c/umocktypes_struct.h
/usr/include/umock_c/umocktypes_wcharptr.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-umock-c/c4770fd76438e6ead5e333d693d65b1b68d924b0
