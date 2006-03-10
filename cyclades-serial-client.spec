# TODO: fix lib install when "%{_lib}" != "lib"
Summary:	Serial Port Interface for RFC 2217 compliant terminal servers
Summary(pl):	Interfejs portów szeregowych dla serwerów terminali zgodnych z RFC 2217
Name:		cyclades-serial-client
Version:	0.93
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client/%{name}-%{version}.tgz
# Source0-md5:	6f43a9b4998ce966b42f12eca12ab3fb
URL:		http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package connects a pseudo-tty on a local system to a remote
serial port.

%description -l pl
Ten pakiet po³±cza pseudoterminal na systemie lokalnym do zdalnego
portu szeregowego.

%prep
%setup -q

%build
%configure
%{__make} \
	CCFLAGS="%{rpmcflags} -Wall -W -Wshadow -Wpointer-arith -Wwrite-strings -pedantic" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/changelog
%attr(755,root,root) %{_sbindir}/cyclades-serial-client
%attr(755,root,root) %{_sbindir}/cyclades-ser-cli
%attr(755,root,root) %{_libdir}/libcyclades-ser-cli.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyclades-devices
%{_mandir}/man[58]/*
