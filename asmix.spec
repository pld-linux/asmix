Summary:	AfterStep sound mixer volume control
Summary(pl):	Mixer dla AfterStepa
Name:		asmix
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.tigr.net/afterstep/download/asmix/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tool displays a volume knob on a ground plate or without a ground
plate if you use -shape option. The volume knob adjusts the master
volume of your sound card. Just grab the knob with the left button of
your mouse and drag it around.

%description -l pl
Kolejny regulator g³o¶no¶ci. Prosty w obs³udze. Przyjemny wygl±d. Du¿±
ga³k± regulujemy poziom sumy. Wygl±da równie dobrze pod AfterStepem
jak pod innymi zarz±dcami okien.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install asmix $RPM_BUILD_ROOT%{_bindir}
install asmix.man $RPM_BUILD_ROOT/%{_mandir}/man1/asmix.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
