Summary:	AfterStep sound mixer volume control
Summary(pl):	Mixer pod AfterStep'a
Name:		asmix
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.tigr.net/afterstep/download/asmix/asmix-1.3.tar.gz
BuildRequires:	autoconf
BuildRequires:	XFree86-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	XFree86

%description

The tool displays a volume knob on a ground plate or without                    
a ground plate if you use -shape option. The volume knob adjusts                
the master volume of your sound card. Just grab the knob with                   
the left button of your mouse and drag it around.

%description -l pl

Kolejny regulator g³o¶no¶ci. Prosty w obs³udze. Przyjemny wygl±d. 
Du¿± ga³k± regulujemy poziom sumy. Wygl±da równie dobrze pod AfterStep'em
jak pod innymi wm'ami.

%prep
%setup -q

%build
%configure2_13
make

%install

mkdir $RPM_BUILD_ROOT/usr/bin -p
mkdir $RPM_BUILD_ROOT/%{_mandir}/man1 -p

mv asmix.man asmix.1

install -c asmix $RPM_BUILD_ROOT/%{_bindir}
install -c asmix.1 $RPM_BUILD_ROOT/%{_mandir}/man1
gzip -9nf CHANGES INSTALL LICENSE README
gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man1/asmix.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
/%{_bindir}/*
%attr(644,root,root)/%{_mandir}/man1/*.gz
