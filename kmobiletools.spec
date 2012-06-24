%bcond_with	debug	# enable debug

%define		_beta _beta1
Summary:	Make your mobile phone communicate with your PC
Summary(de):	L�sst dein Handy mit dem PC kommunizieren
Summary(pl):	Narz�dzie do komunikacji mi�dzy telefonem kom�rkowym a PC
Name:		kmobiletools
Version:	0.5
Release:	0.%{_beta}.2
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/kmobiletools/%{name}-%{version}%{_beta}.tar.bz2
# Source0-md5:	f612c6e0e3007eb9a7fe318a4d17a297
Patch0:		%{name}-desktop.patch
URL:		http://www.kmobiletools.org/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make your mobile phone communicate with your PC.

%description -l de
L�sst dein Handy mit dem PC kommunizieren.

%description -l pl
Narz�dzie do komunikacji mi�dzy telefonem kom�rkowym a PC.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p0

%build
%configure \
	--%{!?with_debug:dis}%{?with_debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f %{name}.lang
%files
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
%{_datadir}/apps/kbluetoothpairingwizard
%{_datadir}/apps/kmtsetup
%{_datadir}/apps/%{name}
%{_datadir}/services/kmobiletools_mainpart.desktop
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde/*.desktop

# -devel (if needed)
#%{_includedir}/kmobiletools

#-kontact (to be done)
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmobiletools.so
%{_libdir}/kde3/libkontact_kmobiletools.la
%{_datadir}/services/kontact/kmobiletools.desktop
