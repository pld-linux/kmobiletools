Summary:	Make your mobile phone communicate with your PC
Summary(pl):	Narzêdzie do komunikacji miêdzy telefonem komórkowym a PC
Name:		kmobiletools
Version:	0.4.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/kmobiletools/%{name}-%{version}.tar.gz
# Source0-md5:	f4be9605142e518ebb61a3f31fc846a5
Patch0:		%{name}-speed.patch
URL:		http://kmobiletools.berlios.de/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make your mobile phone communicate with your PC.

%description -l pl
Narzêdzie do komunikacji miêdzy telefonem komórkowym a PC.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kmobiletools
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde/*.desktop
