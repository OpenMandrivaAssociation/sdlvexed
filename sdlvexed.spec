%define name sdlvexed
%define version 0.6
%define release %mkrel 3

Summary: Vexed is a colourful puzzle
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Games/Puzzles
Url: http://core.segfault.pl/~krzynio/vexed/
BuildRequires: ImageMagick
BuildArch: noarch

%description

SDL Vexed is a puzzle game written in Perl-SDL. It is a clone of the
classic PalmOS game Vexed.

%prep
%setup -q

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
mkdir -p $RPM_BUILD_ROOT{%{_menudir},%_liconsdir,%_miconsdir}
cat > %buildroot%_menudir/%name << EOF
?package(%{name}):command="%{_gamesbindir}/%name" \
		  icon="%name.png" \
		  needs="x11" \
		  section="More Applications/Games/Puzzles" \
		  title="SDL Vexed" \
		  longtitle="Colourful puzzle game" xdg="true"
EOF
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
Categories=X-MandrivaLinux-MoreApplications-Games-Puzzles;Game;LogicGame;
EOF

convert -scale 48x48 gfx/block1.png %buildroot%_liconsdir/%name.png
convert -scale 32x32 gfx/block1.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 gfx/block1.png %buildroot%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc CHANGELOG README*
%_gamesbindir/%name
%_gamesdatadir/%name
%_datadir/applications/mandriva*
%_menudir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
