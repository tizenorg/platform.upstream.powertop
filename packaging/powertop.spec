Name:           powertop
Version:        2.3
Release:        1
License:        GPL-2.0
Summary:        PowerTop is tool that is used for power diagnostics
Url:            http://www.01.org
Group:          Platform Development/Tools
Source0:        https://01.org/powertop/sites/default/files/downloads/%{name}-%{version}.tar.gz
Source1001: 	powertop.manifest

BuildRequires:  gettext
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libnl-1)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(ncurses)

%description
PowerTop is tool that detects which Linux programs
and kernel tunables are resulting in the largest
power consumption and use of battery time. By
fixing (or closing) these applications or
processes, you can immediately see the power
savings in the tool. You'll also see the estimated
time left for battery power if you are running a
laptop.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name}

%lang_package

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_sbindir}/powertop
%{_mandir}/man8/powertop.8.gz
