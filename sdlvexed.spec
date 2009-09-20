%define name sdlvexed
%define version 0.6
%define release %mkrel 9

Summary: Colourful puzzle
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
#gw from Gentoo, make it run again:
#http://bugs.gentoo.org/show_bug.cgi?id=155934
#https://qa.mandriva.com/show_bug.cgi?id=49432
Patch: sdlvexed-new-perl-sdl.patch
License: GPLv2+
Group: Games/Puzzles
#Url: http://core.segfault.pl/~krzynio/vexed/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: imagemagick
BuildArch: noarch

%description
SDL Vexed is a puzzle game written in Perl-SDL. It is a clone of the
classic PalmOS game Vexed.

%prep
%setup -q
%patch

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot{%_gamesbindir,%_gamesdatadir/%name}
cp -r gfx/  levelpacks/ vexed %buildroot%_gamesdatadir/%name
cat > %buildroot%_gamesbindir/%name << EOF
#!/bin/sh
cd %_gamesdatadir/%name
./vexed
EOF
chmod 755 %buildroot%_gamesbindir/%name %buildroot%_gamesdatadir/%name/vexed
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=SDL Vexed
Comment=Colourful puzzle game
Exec=%_gamesbindir/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;LogicGame;
EOF

mkdir -p %buildroot{%_liconsdir,%_miconsdir}
convert -scale 48x48 gfx/block1.png %buildroot%_liconsdir/%name.png
convert -scale 32x32 gfx/block1.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 gfx/block1.png %buildroot%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc CHANGELOG README*
%_gamesbindir/%name
%_gamesdatadir/%name
%_datadir/applications/mandriva*
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
