Summary:	Synce-hal
Summary(pl.UTF-8):	Synce-hal
Name:		synce-hal
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	06c7fe3d2b9c130cd485272d6756f599
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	gnet-devel
BuildRequires:	libmimedir-vlm-devel
BuildRequires:	libtool
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-libsynce-devel >= 0.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synce-hal is a connection framework and dccm-implementation for Windows
Mobile devices that integrates with HAL.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q haldaemon restart

%files
%defattr(644,root,root,755)
%doc README TODO AUTHORS COPYING NEWS ChangeLog
%attr(755,root,root) %{_libdir}/hal-synce-rndis
%attr(755,root,root) %{_libdir}/hal-synce-serial
%attr(755,root,root) %{_libdir}/hal-dccm
%attr(755,root,root) %{_libdir}/synce-serial-chat
%{_datadir}/hal/fdi/policy/20thirdparty/*synce.fdi
