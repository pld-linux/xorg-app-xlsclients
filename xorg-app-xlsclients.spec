Summary:	xlsclients application to list client applications running on a display
Summary(pl.UTF-8):	Aplikacja xlsclients do wypisywania aplikacji klienckich działających na ekranie
Name:		xorg-app-xlsclients
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xlsclients-%{version}.tar.bz2
# Source0-md5:	6d42621616da0c720f640d23873604ce
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xlsclients application is a utility for listing information about the
client applications running on a X11 server.

%description -l pl.UTF-8
Aplikacja xlsclients to narzędzie do wypisywania informacji o
aplikacjach klienckich uruchomionych na serwerze X11.

%prep
%setup -q -n xlsclients-%{version}

%build
%{__aclocal}
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

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1x*
