Name:           powertop
Version:        2.5
Release:        1
License:        GPL-2.0
Summary:        A tool that is used for power diagnostics
Url:            http://www.01.org
Group:          System/Utilities
Source0:        https://01.org/powertop/sites/default/files/downloads/%{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  gettext
BuildRequires:  pkgconfig(libnl-1)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)

%description
PowerTop is a tool that detects which Linux programs
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

%docs_package

%lang_package

%files
%manifest %{name}.manifest
%license COPYING
%{_sbindir}/powertop
