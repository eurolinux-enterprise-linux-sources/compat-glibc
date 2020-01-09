%define glibcsrcdir glibc-2.12-2-gc4ccff1
%define glibcversion 2.12
### glibc.spec.in follows:
%define run_glibc_tests 1
%define auxarches noarch
%define xenarches noarch
%define buildxen 0
%define xenpackage 0
%define buildpower6 0
%define rtkaioarches noarch
%define debuginfocommonarches noarch
%define _unpackaged_files_terminate_build 0
%undefine _enable_debug_packages
# What's the right thing to do with these?
# XXX
%define biarcharches noarch
%define multiarcharches noarch
%define systemtaparches noarch
# XXX

Summary: Compatibility C library
Name: compat-glibc
# XXX Should this bump?
Epoch: 1
Version: %{glibcversion}
Release: 4%{?dist}
# GPLv2+ is used in a bunch of programs, LGPLv2+ is used for libraries.
# Things that are linked directly into dynamically linked programs
# and shared libraries (e.g. crt files, lib*_nonshared.a) have an additional
# exception which allows linking it into any kind of programs or shared
# libraries without restrictions.
License: LGPLv2+ and LGPLv2+ with exceptions and GPLv2+
Group: Development/Libraries
URL: http://sources.redhat.com/glibc/
Source0: %{?glibc_release_url}%{glibcsrcdir}.tar.bz2
Source1: %{glibcsrcdir}-fedora.tar.bz2
Source2: dummylib.sh
Patch0: glibc-fedora.patch
Patch1: glibc-ia64-lib64.patch
Patch2: glibc-rh587360.patch
Patch3: glibc-rh582738.patch
Patch4: glibc-getlogin-r.patch
Patch5: glibc-localedata.patch
Patch6: glibc-rh593396.patch
Patch7: glibc-recvmmsg.patch
Patch8: glibc-aliasing.patch
Patch9: glibc-rh593686.patch
Patch10: glibc-rh607461.patch
Patch11: glibc-rh621959.patch
Patch12: glibc-rh607010.patch
Patch13: glibc-rh630801.patch
Patch14: glibc-rh631011.patch
Patch15: glibc-rh641128.patch
Patch16: glibc-rh642584.patch
Patch17: glibc-rh643822.patch
Patch18: glibc-rh645672.patch
Patch19: glibc-rh580498.patch
Patch20: glibc-rh615090.patch
Patch21: glibc-rh623187.patch
Patch22: glibc-rh646954.patch
Patch23: glibc-rh647448.patch
Patch24: glibc-rh615701.patch
Patch25: glibc-rh652661.patch
Patch26: glibc-rh656530.patch
Patch27: glibc-rh656014.patch
Patch28: glibc-rh661982.patch
Patch29: glibc-rh601686.patch
Patch30: glibc-rh676076.patch
Patch31: glibc-rh667974.patch
Patch32: glibc-rh625893.patch
Patch33: glibc-rh681054.patch
Patch34: glibc-rh689471.patch
Patch35: glibc-rh692177.patch
Patch36: glibc-rh692838.patch
Patch37: glibc-rh703480.patch
Patch38: glibc-rh705465.patch
Patch39: glibc-rh703481.patch
Patch40: glibc-rh694386.patch
Patch41: glibc-rh676591.patch
Patch42: glibc-rh711987.patch
Patch43: glibc-rh695595.patch
Patch45: glibc-rh695963.patch
Patch46: glibc-rh713134.patch
Patch47: glibc-rh714823.patch
Patch48: glibc-rh718057.patch
Patch49: glibc-rh688980.patch
Patch50: glibc-rh712248.patch
Patch51: glibc-rh731042.patch
Patch52: glibc-rh730379.patch
Patch53: glibc-rh700507.patch
Patch54: glibc-rh699724.patch
Patch55: glibc-rh736346.patch
Patch56: glibc-rh737778.patch
Patch57: glibc-rh738665.patch
Patch58: glibc-rh738763.patch
Patch59: glibc-rh739184.patch
Patch60: glibc-rh711927.patch
Patch61: glibc-rh688720.patch
Patch62: glibc-rh726517.patch
Patch63: glibc-rh752122.patch
Patch64: glibc-rh739971.patch
Patch65: glibc-rh751750.patch
Patch66: glibc-rh740506.patch
Patch67: glibc-rh757888.patch
Patch68: glibc-rh750531.patch
Patch69: glibc-rh749188.patch
Patch70: glibc-rh767746.patch
Patch72: glibc-rh767693.patch
Patch73: glibc-rh740506-2.patch
Patch74: glibc-rh696472.patch
Patch75: glibc-rh771342.patch
Patch76: glibc-rh657572.patch
Patch77: glibc-rh767693-2.patch
Patch78: glibc-rh782585.patch
Patch79: glibc-rh784402.patch
Patch80: glibc-rh697421.patch
Patch81: glibc-rh785984.patch
Patch82: glibc-rh767146.patch
Patch83: glibc-rh766513.patch
Patch84: glibc-rh789209.patch
Patch85: glibc-rh788959.patch
Patch86: glibc-rh789189.patch
Patch88: glibc-rh789238.patch
Patch89: glibc-rh794817.patch
Patch90: glibc-rh797094-1.patch
Patch91: glibc-rh797094-2.patch
Patch92: glibc-rh789238-2.patch
Patch93: glibc-rh795498.patch
Patch94: glibc-rh794817-2.patch
Patch95: glibc-rh804689.patch
Patch96: glibc-rh809602.patch
Patch97: glibc-rh808337.patch
Patch98: glibc-rh804630.patch
Patch99: glibc-rh788959-2.patch
Patch100: glibc-rh808545.patch

Patch10000: glibc-fix-implicit-rule.patch
Patch10001: glibc-gcc47-ctordtor.patch
Patch10002: glibc-rh783979.patch

# I'm not sure why we didn't see strict aliasing warnings with RHEL 6 builds, perhaps
# it's due to the newer compiler in RHEL 7.
Patch10003: glibc-rh883974.patch

# GCC recently removed -mnew-mnemonics for PPC
Patch10004: glibc-ppc-mnemonics.patch

# Disable -ftree-loop-distribute-patterns  which converts open code to
# memset, memcpy, etc.  This can cause infinte loops when compiling those
# routines in glibc.  Furthermore it can create calls through the PLT in 
# the dynamic linker when the PLT hasn't been set up yet.
Patch10005: glibc-rh911307.patch

# Newer compiler is also complaining about overflow problems
Patch10006: glibc-rh883974-2.patch

# Fix namespace conflict with Altivec
Patch10007: glibc-rh1048853.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Autoreq: true
Autoprov: false
Requires: compat-glibc-headers = %{epoch}:%{version}-%{release}
# This is for building auxiliary programs like memusage, nscd
# For initial glibc bootstraps it can be commented out
BuildRequires: gd-devel libpng-devel zlib-devel texinfo, libselinux-devel >= 1.33.4-3
BuildRequires: audit-libs-devel >= 1.1.3, sed >= 3.95, libcap-devel, gettext, nss-devel
BuildRequires: /bin/ps, /bin/kill, /bin/awk
%ifarch %{systemtaparches}
BuildRequires: systemtap-sdt-devel
%endif
# This is to ensure that __frame_state_for is exported by glibc
# will be compatible with egcs 1.x.y
BuildRequires: gcc >= 3.2
%define enablekernel 2.6.18
%ifarch i386
%define nptl_target_cpu i486
%else
%define nptl_target_cpu %{_target_cpu}
%endif
%ifarch %{multiarcharches}
# Need STT_IFUNC support
%ifarch ppc ppc64
BuildRequires: binutils >= 2.20.51.0.2
Conflicts: binutils < 2.20.51.0.2
%else
BuildRequires: binutils >= 2.19.51.0.10
Conflicts: binutils < 2.19.51.0.10
%endif
# Earlier releases have broken support for IRELATIVE relocations
Conflicts: prelink < 0.4.2
%else
# Need AS_NEEDED directive
# Need --hash-style=* support
BuildRequires: binutils >= 2.17.50.0.2-5
%endif
BuildRequires: gcc >= 3.2.1-5
%ifarch ppc s390 s390x
BuildRequires: gcc >= 4.1.0-0.17
%endif
%if 0%{?_enable_debug_packages}
BuildRequires: elfutils >= 0.72
BuildRequires: rpm >= 4.2-0.56
%endif
%define __find_provides %{_builddir}/%{glibcsrcdir}/find_provides.sh
%define _filter_GLIBC_PRIVATE 1

%description
This package contains stub shared libraries and static libraries
from Red Hat Enterprise Linux 6.

To compile and link against these compatibility libraries, use
gcc -fgnu89-inline \
      -I %{_prefix}/lib/%{_target_cpu}-redhat-linux6E/include \
      -B %{_prefix}/lib/%{_target_cpu}-redhat-linux6E/%{_lib}/


%package headers
Summary: Header files for development using standard C libraries.
Group: Development/Libraries
Provides: %{name}-headers(%{_target_cpu})
Requires: compat-glibc = %{epoch}:%{version}-%{release}
%ifarch x86_64
# If both -m32 and -m64 is to be supported on AMD64, x86_64 glibc-headers
# have to be installed, not i586 ones.
Obsoletes: %{name}-headers(i586)
Obsoletes: %{name}-headers(i686)
%endif
Requires(pre): kernel-headers
Requires: kernel-headers >= 2.2.1
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: kernel-headers >= 2.6.22

%description headers
The compat-glibc-headers package contains the header files from
Red Hat Enterprise Linux 56


%prep
%setup -q -n %{glibcsrcdir} -b1
%patch0 -E -p1
%ifarch ia64
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1

# These are compat-glibc specific changes necessary for the old glibc to
# build with new compilers.
%patch10000 -p1
%patch10001 -p1
%patch10002 -p1
%patch10003 -p1
%patch10004 -p1
%patch10005 -p1
%patch10006 -p1
%patch10007 -p1

find . -type f -size 0 -o -name "*.orig" -exec rm -f {} \;
touch `find . -name configure`
touch locale/programs/*-kw.h

%build
GCC=gcc
GXX=g++
%ifarch %{ix86}
BuildFlags="-march=%{nptl_target_cpu} -mtune=generic"
%endif
%ifarch i686
BuildFlags="-march=i686 -mtune=generic"
%endif
%ifarch i386 i486 i586
BuildFlags="$BuildFlags -mno-tls-direct-seg-refs"
%endif
%ifarch x86_64
BuildFlags="-mtune=generic"
%endif
%ifarch alphaev6
BuildFlags="-mcpu=ev6"
%endif
%ifarch sparc
BuildFlags="-fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparcv9
BuildFlags="-mcpu=ultrasparc -fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparcv9v
BuildFlags="-mcpu=niagara -fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparc64
BuildFlags="-mcpu=ultrasparc -mvis -fcall-used-g6"
GCC="gcc -m64"
GXX="g++ -m64"
%endif
%ifarch sparc64v
BuildFlags="-mcpu=niagara -mvis -fcall-used-g6"
GCC="gcc -m64"
GXX="g++ -m64"
%endif
%ifarch ppc64
BuildFlags="-mno-minimal-toc"
GCC="gcc -m64"
GXX="g++ -m64"
%endif

BuildFlags="$BuildFlags -fgnu89-inline"
# Add -DNDEBUG unless using a prerelease
case %{version} in
  *.*.9[0-9]*) ;;
  *)
     BuildFlags="$BuildFlags -DNDEBUG"
     ;;
esac
EnableKernel="--enable-kernel=%{enablekernel}"
echo "$GCC" > Gcc
AddOns=`echo */configure | sed -e 's!/configure!!g;s!\(linuxthreads\|nptl\|rtkaio\|powerpc-cpu\)\( \|$\)!!g;s! \+$!!;s! !,!g;s!^!,!;/^,\*$/d'`
%ifarch %{rtkaioarches}
AddOns=,rtkaio$AddOns
%endif

build_nptl()
{
builddir=build-%{nptl_target_cpu}-$1
shift
rm -rf $builddir
mkdir $builddir ; cd $builddir
build_CFLAGS="$BuildFlags -g -O3 $*"
../configure CC="$GCC" CXX="$GXX" CFLAGS="$build_CFLAGS" \
	--prefix=%{_prefix} \
	--enable-add-ons=nptl$AddOns --without-cvs $EnableKernel \
	--without-selinux \
	--with-headers=%{_prefix}/include --enable-bind-now \
	--with-tls --with-__thread --build %{nptl_target_cpu}-redhat-linux \
	--host %{nptl_target_cpu}-redhat-linux \
%ifarch %{multiarcharches}
	--enable-multi-arch \
%endif
%ifarch %{systemtaparches}
	--enable-systemtap \
%endif
	--disable-profile --enable-experimental-malloc --enable-nss-crypt

make %{?_smp_mflags} -r CFLAGS="$build_CFLAGS" PARALLELMFLAGS=-s

cd ..
}

build_nptl linuxnptl

%install
GCC=`cat Gcc`

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make -j1 install_root=$RPM_BUILD_ROOT install -C build-%{nptl_target_cpu}-linuxnptl PARALLELMFLAGS=-s
chmod +x $RPM_BUILD_ROOT%{_prefix}/libexec/pt_chown
%ifnarch %{auxarches}
cd build-%{nptl_target_cpu}-linuxnptl && \
  make %{?_smp_mflags} install_root=$RPM_BUILD_ROOT install-locales -C ../localedata objdir=`pwd` && \
  cd ..
%endif

# Remove the files we don't want to distribute
rm -f $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libNoVersion*
rm -f $RPM_BUILD_ROOT/%{_lib}/libNoVersion*
rm -f $RPM_BUILD_ROOT{%{_prefix},}/%{_lib}/lib{NoVersion,nss,BrokenLocale}*

# NPTL <bits/stdio-lock.h> is not usable outside of glibc, so include
# the generic one (#162634)
cp -a bits/stdio-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/stdio-lock.h
# And <bits/libc-lock.h> needs sanitizing as well.
cp -a fedora/libc-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/libc-lock.h

ln -sf libbsd-compat.a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libbsd.a

strip -g $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.o

# rquota.x and rquota.h are now provided by quota
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

COMPATD=$RPM_BUILD_ROOT%{_prefix}/lib/%{_target_cpu}-redhat-linux6E

mkdir -p $COMPATD/%{_lib}

mv -f $RPM_BUILD_ROOT%{_prefix}/include $COMPATD/
mv -f $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.[oa] $COMPATD/%{_lib}
strip -R .comment -g $COMPATD/%{_lib}/*.a
ln -sf libbsd-compat.a $COMPATD/%{_lib}/libbsd.a
mkdir -p $RPM_BUILD_ROOT%{_prefix}/tmp
cp -a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.so $RPM_BUILD_ROOT%{_prefix}/tmp
rm -f $RPM_BUILD_ROOT%{_prefix}/tmp/libc.so
rm -f $RPM_BUILD_ROOT%{_prefix}/tmp/libpthread.so
pushd $RPM_BUILD_ROOT%{_prefix}/tmp
ln -sf ../../%{_lib}/libc.so.6* libc.so
ln -sf ../../%{_lib}/libpthread.so.0* libpthread.so
popd

cd build-%{nptl_target_cpu}-linuxnptl
for libpath in $RPM_BUILD_ROOT%{_prefix}/tmp/*.so; do
  lib=`basename $libpath .so`
  sh %{SOURCE2} $libpath $COMPATD/%{_lib}/$lib.so $lib.map
done

mv $COMPATD/%{_lib}/libc.so $COMPATD/%{_lib}/libc_real.so
mv $COMPATD/%{_lib}/libpthread.so $COMPATD/%{_lib}/libpthread_real.so
LDIR=%{_prefix}/lib/%{_target_cpu}-redhat-linux6E/%{_lib}
sed 's~^GROUP.*$~GROUP ('$LDIR'/libc_real.so '$LDIR'/libc_nonshared.a )~' \
  $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libc.so > $COMPATD/%{_lib}/libc.so
sed 's~^GROUP.*$~GROUP ('$LDIR'/libpthread_real.so '$LDIR'/libpthread_nonshared.a )~' \
  $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libpthread.so > $COMPATD/%{_lib}/libpthread.so

%clean
rm -rf "$RPM_BUILD_ROOT"

%files 
%defattr(-,root,root)
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux6E
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux6E/%{_lib}
%{_prefix}/lib/%{_target_cpu}-redhat-linux6E/%{_lib}/*.[oa]
%{_prefix}/lib/%{_target_cpu}-redhat-linux6E/%{_lib}/*.so

%files headers
%defattr(-,root,root)
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux6E
%{_prefix}/lib/%{_target_cpu}-redhat-linux6E/include


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1:2.12-4
- Mass rebuild 2014-01-24

* Tue Jan  7 2014 Siddhesh Poyarekar <siddhesh@redhat.com> - 1:2.12-3
- Fix namespace conflict with Altivec (#1048853).

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:2.12-2
- Mass rebuild 2013-12-27

* Fri Jul 19 2013 Jeff Law <law@redhat.com> - 1:2.12-1.80.5
- Backport timezone/zic.c change to avoid overflow in oadd (#883974) 

* Tue May 28 2013 Jeff Law <law@redhat.com> - 1:2.12-1.80.4
- Fix passing of -z execstack to the linker.
- Remove -mnew-mnenomics from PPC build flags
- Pull over patch for 911307 from Fedora

* Mon May 20 2013 Jeff Law <law@redhat.com> - 1:2.12-1.80.3
- Add -z execstack to command line for building DSOs in
  dummylib.sh (#883974)

* Wed Jan 2 2013 Jeff Law <law@redhat.com> - 1:2.12-1.80.2
- Backport change to avoid strict-aliasing problems in 
  md5.c (#883974)

* Wed Jun 13 2012 Daniel Mach <dmach@redhat.com> - 1:2.12-1.80.1
- add missing epoch to Requires: in headers package

* Fri Jun 8 2012 Jeff Law <law@redhat.com> - 1:2.12-1.80
- changed into compatibility package
