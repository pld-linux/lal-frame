# TODO: framec support (BR: pkgconfig(framecppc) >= 2.0.0)
Summary:	LAL wrapping of the LILO/Virgo Frame library
Summary(pl.UTF-8):	Obudowanie LAL do biblioteki LILO/Virgo Frame
Name:		lal-frame
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.ligo.org/lscsoft/source/lalsuite/lalframe-%{version}.tar.xz
# Source0-md5:	f7e471322ac062c0bc9ffd3179b770fb
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/DASWG/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	lal-devel >= 6.18.0
BuildRequires:	libframe-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-numpy-devel >= 1:1.7
BuildRequires:	swig >= 3.0.12
BuildRequires:	swig-python >= 2.0.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	lal >= 6.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL wrapping of the LILO/Virgo Frame library.

%description -l pl.UTF-8
Obudowanie LAL do biblioteki LILO/Virgo Frame.

%package devel
Summary:	Header files for lal-frame library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-frame
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lal-devel >= 6.18.0
Requires:	libframe-devel

%description devel
Header files for lal-frame library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-frame.

%package static
Summary:	Static lal-frame library
Summary(pl.UTF-8):	Statyczna biblioteka lal-frame
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-frame library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-frame.

%package -n octave-lalframe
Summary:	Octave interface for LAL Frame
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL Frame
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave-lal >= 6.18.0

%description -n octave-lalframe
Octave interface for LAL Frame.

%description -n octave-lalframe -l pl.UTF-8
Interfejs Octave do biblioteki LAL Frame.

%package -n python-lalframe
Summary:	Python bindings for LAL Frame
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Frame
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-lal >= 6.18.0
Requires:	python-modules >= 1:2.6

%description -n python-lalframe
Python bindings for LAL Frame.

%description -n python-lalframe -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Frame.

%prep
%setup -q -n lalframe-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalframe.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lalfr-*
%attr(755,root,root) %{_bindir}/lalframe_version
%attr(755,root,root) %{_libdir}/liblalframe.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalframe.so.10
/etc/shrc.d/lalframe-user-env.csh
/etc/shrc.d/lalframe-user-env.fish
/etc/shrc.d/lalframe-user-env.sh
%{_mandir}/man1/lalfr-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalframe.so
%{_includedir}/lal/Aggregation.h
%{_includedir}/lal/FrameCalibration.h
%{_includedir}/lal/LALFrStream.h
%{_includedir}/lal/LALFrame*.h
%{_includedir}/lal/SWIGLALFrame*.h
%{_includedir}/lal/SWIGLALFrame*.i
%{_includedir}/lal/swiglalframe.i
%{_pkgconfigdir}/lalframe.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalframe.a

%files -n octave-lalframe
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalframe.oct

%files -n python-lalframe
%defattr(644,root,root,755)
%dir %{py_sitedir}/lalframe
%attr(755,root,root) %{py_sitedir}/lalframe/_lalframe.so
%{py_sitedir}/lalframe/*.py[co]
%{py_sitedir}/lalframe/utils
