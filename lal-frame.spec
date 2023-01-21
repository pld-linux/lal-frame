# TODO: framec support (BR: pkgconfig(framecppc) >= 2.5.5)
Summary:	LAL wrapping of the LILO/Virgo Frame library
Summary(pl.UTF-8):	Obudowanie LAL do biblioteki LILO/Virgo Frame
Name:		lal-frame
Version:	2.0.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalframe-%{version}.tar.xz
# Source0-md5:	e25492953f9f8c065b0e528d4658f951
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/DASWG/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	lal-devel >= 7.2.2
BuildRequires:	libframe-devel >= 8.39.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 2.0.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	lal >= 7.2.2
Requires:	libframe >= 8.39.2
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
Requires:	lal-devel >= 7.2.2
Requires:	libframe-devel >= 8.39.2

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
Requires:	octave-lal >= 7.2.2

%description -n octave-lalframe
Octave interface for LAL Frame.

%description -n octave-lalframe -l pl.UTF-8
Interfejs Octave do biblioteki LAL Frame.

%package -n python3-lalframe
Summary:	Python bindings for LAL Frame
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Frame
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 7.2.2
Requires:	python3-modules >= 1:3.5
Obsoletes:	python-lalframe < 1.5

%description -n python3-lalframe
Python bindings for LAL Frame.

%description -n python3-lalframe -l pl.UTF-8
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lalfr-*
%attr(755,root,root) %{_bindir}/lalframe_version
%attr(755,root,root) %{_libdir}/liblalframe.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalframe.so.13
/etc/shrc.d/lalframe-user-env.csh
/etc/shrc.d/lalframe-user-env.fish
/etc/shrc.d/lalframe-user-env.sh
%{_mandir}/man1/lalfr-*.1*
%{_mandir}/man1/lalframe_version.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalframe.so
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

%files -n python3-lalframe
%defattr(644,root,root,755)
%dir %{py3_sitedir}/lalframe
%attr(755,root,root) %{py3_sitedir}/lalframe/_lalframe.so
%{py3_sitedir}/lalframe/*.py
%{py3_sitedir}/lalframe/__pycache__
%dir %{py3_sitedir}/lalframe/utils
%{py3_sitedir}/lalframe/utils/*.py
%{py3_sitedir}/lalframe/utils/__pycache__
