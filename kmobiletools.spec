#
# Conditional build:
%bcond_without	kdebluetooth	# don't build kdebluetooth integration
%bcond_without	obexftp		# don't build FileSystem integration
%bcond_without	gammu		# build gammu integration

%define		subver	beta3
%define		rel		5

Summary:	Make your mobile phone communicate with your PC
Summary(de.UTF-8):	Lässt dein Handy mit dem PC kommunizieren
Summary(pl.UTF-8):	Narzędzie do komunikacji między telefonem komórkowym a PC
Name:		kmobiletools
Version:	0.5.0
Release:	0.%{subver}.%{rel}
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/kmobiletools/%{name}-%{version}-%{subver}.tar.bz2
# Source0-md5:	2880ca9b21ba4f70088be64b6ef6a39b
Patch0:		%{name}-desktop.patch
Patch1:		kde-ac260-lt.patch
Patch2:		%{name}-configure_in_in.patch
Patch3:		%{name}-device_data.patch
URL:		http://www.kmobiletools.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gammu:BuildRequires:	gammu-devel >= 1.10.5}
%{?with_gammu:BuildRequires:	gammu-devel < 1:1.12.0}
%{?with_kdebluetooth:BuildRequires:	kdebluetooth-devel}
BuildRequires:	kdelibs-devel
BuildRequires:	kdepim-devel
%{?with_obexftp:BuildRequires:	obexftp-devel}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make your mobile phone communicate with your PC.

%description -l de.UTF-8
Lässt dein Handy mit dem PC kommunizieren.

%description -l pl.UTF-8
Narzędzie do komunikacji między telefonem komórkowym a PC.

%package devel
Summary:	Header files for kmobiletools
Summary(es.UTF-8):	Arquivos de cabeçalho para kmobiletools
Summary(pl.UTF-8):	Pliki nagłówkowe do kmobiletools
Summary(pt_BR.UTF-8):	Arquivos de inclusão para a kmobiletools
Summary(ru.UTF-8):	Хедеры для kmobiletools
Summary(uk.UTF-8):	Хедери для kmobiletools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for kmobiletools.

%description devel -l pl.UTF-8
Pliki nagłówkowe do kmobiletools.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with%{!?with_gammu:out}-gammu \
	--with%{!?with_obexftp:out}-obexftp \
	--enable-kontact-plugin \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kmobiletools
%attr(755,root,root) %{_bindir}/kbluetoothpairingwizard
%attr(755,root,root) %{_bindir}/kmtsetup
%{_libdir}/kde3/libkmobiletoolsdevicepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmobiletoolsdevicepart.so
%{_libdir}/kde3/libkmobiletoolsmainpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmobiletoolsmainpart.so
%{_libdir}/libkmobiletools.la
%attr(755,root,root) %{_libdir}/libkmobiletools.so
%{_libdir}/libkmobiletools_at.la
%attr(755,root,root) %{_libdir}/libkmobiletools_at.so

%if %{with gammu}
%{_libdir}/libkmobiletools_gammu.la
%attr(755,root,root) %{_libdir}/libkmobiletools_gammu.so
%{_datadir}/services/gammu_engine.desktop
%endif

%if %{with obexftp}
%{_libdir}/kde3/kio_mobile.la
%attr(755,root,root) %{_libdir}/kde3/kio_mobile.so
%{_libdir}/kde3/kio_obex2.la
%attr(755,root,root) %{_libdir}/kde3/kio_obex2.so
%{_datadir}/services/mobile.protocol
%{_datadir}/services/obex2.protocol
%{_datadir}/apps/systemview/mobile.desktop
%endif

%{_datadir}/apps/kbluetoothpairingwizard
%{_datadir}/apps/kmtsetup
%{_datadir}/apps/%{name}
%{_datadir}/services/kmobiletools_mainpart.desktop
%{_datadir}/services/at_engine.desktop
%{_datadir}/servicetypes/kmobiletoolsengine.desktop

%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde/*.desktop

#-kontact (to be done)
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmobiletools.so
%{_libdir}/kde3/libkontact_kmobiletools.la
%{_datadir}/services/kontact/kmobiletools.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/kmobiletools
