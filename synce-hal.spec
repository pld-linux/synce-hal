# TODO:
#	package bluetooth stuff
Summary:	Synce-hal
Summary(pl.UTF-8):	Synce-hal
Name:		synce-hal
Version:	0.15
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	796eca27a2ce561247e7a71375c242b6
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	gnet-devel
BuildRequires:	hal-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-libsynce-devel >= 0.12
Obsoletes:	synce-odccm < %{version}-%{release}
Obsoletes:	synce-serial < %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		haldir	%{_libdir}/hal

%description
Synce-hal is a connection framework and dccm-implementation for
Windows Mobile devices that integrates with HAL.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-hal-addon-dir=%{haldir}/scripts

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	haldir=%{haldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q haldaemon restart

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.Hal.Device.Synce.conf
%attr(755,root,root) %{_bindir}/synce-unlock.py
%attr(755,root,root) %{_libdir}/hal-dccm
%attr(755,root,root) %{_libdir}/synce-serial-chat
%{_datadir}/hal/fdi/policy/20thirdparty/*synce.fdi
%dir %{_datadir}/synce-hal
%{_datadir}/synce-hal/dhclient.conf
%attr(755,root,root) %{haldir}/hal-synce-rndis
%attr(755,root,root) %{haldir}/hal-synce-serial
