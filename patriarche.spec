%define name patriarche
%define version 0.2.8
%define release %mkrel 12
%define bookname Le Patriarche

Summary: The true story of Ylraw
Name: %name
Version: %version
Release: %release
License: GPL
Epoch: 1
url: https://perso.wanadoo.fr/warly/files/patriarche
Source: %name-%version.tar.bz2
Patch: patriarche-0.2.8-use-gimp26.patch
Patch1: patriarche-fix-bz2-images.patch

Group: Books/Literature
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: libxslt-proc gimp tetex-dvipdfm tetex-latex
BuildRequires:  x11-server-xvfb

%description
Le Patriarche postscript versions

%package html
Summary: The true story of Ylraw
Group: Books/Literature

%description html
Le Patriarche html versions.

%package pdf
Summary: The true story of Ylraw
Group: Books/Literature

%description pdf
Le Patriarche pdf versions.

%package txt
Summary: The true story of Ylraw
Group: Books/Literature

%description txt
Le Patriarche text versions.

%package xml
Summary: The true story of Ylraw
Group: Books/Literature

%description xml
Le Patriarche xml source versions.

%package en
Summary: The true story of Ylraw
Group: Books/Literature

%description en
Le Patriarche postscript versions

%package html-en
Summary: The true story of Ylraw
Group: Books/Literature

%description html-en
Le Patriarche html versions.

%package pdf-en
Summary: The true story of Ylraw
Group: Books/Literature

%description pdf-en
Le Patriarche pdf versions.

%package txt-en
Summary: The true story of Ylraw
Group: Books/Literature

%description txt-en
Le Patriarche text versions.

%package xml-en
Summary: The true story of Ylraw
Group: Books/Literature

%description xml-en
Le Patriarche xml source versions.

%package tools
License: GPL
Summary: patriarche related xml/text tools
Group: Publishing

%description tools
Tools needed to construct patriarche-like book.

%prep
%setup -q
%patch -p0
%patch1 -p0
bunzip2 img/*.bz2
gunzip  img/*.gz

%build
XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%{_bindir}/Xvfb :$XDISPLAY &
export DISPLAY=:$XDISPLAY
export GIMP2_DIRECTORY=%{_builddir}/%{name}-%{version}/gimp-2.6
make
kill $(cat /tmp/.X$XDISPLAY-lock) ||:

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT

# Menu fr
install -d -m 755 $RPM_BUILD_ROOT%{_menudir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-1.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 postscript
Comment=%{bookname} Tome 1 Le Premier Monde - À la recherche d'un Dieu
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.1.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-2.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 postscript
Comment=%{bookname} Tome 2 Le Premier Monde - Le bien
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.2.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-3.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 postscript
Comment=%{bookname} Tome 3 Le Premier Monde - Crise
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.3.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-4.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 postscript
Comment=%{bookname} Tome 4 Le Premier Monde - Ménocha
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.4.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-1.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 PDF
Comment=%{bookname} Tome 1 Le Premier Monde - À la recherche d'un Dieu
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.1.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-2.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 PDF
Comment=%{bookname} Tome 2 Le Premier Monde - Le bien
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.2.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-3.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 PDF
Comment=%{bookname} Tome 3 Le Premier Monde - Crise
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.3.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-4.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 PDF
Comment=%{bookname} Tome 4 Le Premier Monde - Ménocha
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.4.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-1.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 HTML
Comment=%{bookname} Tome 1 Le Premier Monde - À la recherche d'un Dieu
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.1-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-2.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 HTML
Comment=%{bookname} Tome 2 Le Premier Monde - Le bien
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.2-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-3.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 HTML
Comment=%{bookname} Tome 3 Le Premier Monde - Crise
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.3-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-4.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 HTML
Comment=%{bookname} Tome 4 Le Premier Monde - Ménocha
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.4-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-1-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 postscript
Comment=%{bookname} Tome 1 The First World: In the search of a God
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.1.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-2-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 postscript
Comment=%{bookname} Tome 2 The First World: Good
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.2.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-3-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 postscript
Comment=%{bookname} Tome 3 The First World: Crisis
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.3.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-ps-4-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 postscript
Comment=%{bookname} Tome 4 The First World - Ménocha
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.4.ps
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-1-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 PDF
Comment=%{bookname} Tome 1 The First World: In the search of a God
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.1.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-2-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 PDF
Comment=%{bookname} Tome 2 The First World: Good
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.2.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-3-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 PDF
Comment=%{bookname} Tome 3 The First World: Crisis
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.3.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-pdf-4-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 PDF
Comment=%{bookname} Tome 4 The First World - Ménocha
Exec=xdg-open %{_datadir}/%name/A4-patriarche-1.4.pdf
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-1-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 1 HTML
Comment=%{bookname} Tome 1 The First World: In the search of a God
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.1-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-2-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 2 HTML
Comment=%{bookname} Tome 2 The First World: Good
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.2-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-3-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 3 HTML
Comment=%{bookname} Tome 3 The First World: Crisis
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.3-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-html-4-en.desktop << EOF
[Desktop Entry]
Name=%{bookname} Tome 4 HTML
Comment=%{bookname} Tome 4 The First World - Ménocha
Exec=www-browser %{_datadir}/%name/i18n/en/html-1.4-en/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%if %mdkversion < 200900
%post pdf
%{update_menus}
%endif

%if %mdkversion < 200900
%postun pdf
%{clean_menus}
%endif

%if %mdkversion < 200900
%post html
%{update_menus}
%endif

%if %mdkversion < 200900
%postun html
%{clean_menus}
%endif

%if %mdkversion < 200900
%post en
%{update_menus}
%endif

%if %mdkversion < 200900
%postun en
%{clean_menus}
%endif

%if %mdkversion < 200900
%post pdf-en
%{update_menus}
%endif

%if %mdkversion < 200900
%postun pdf-en
%{clean_menus}
%endif

%if %mdkversion < 200900
%post html-en
%{update_menus}
%endif

%if %mdkversion < 200900
%postun html-en
%{clean_menus}
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-ps-?.desktop
%{_datadir}/patriarche/A4-patriarche-*.ps

%files pdf
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-pdf-?.desktop
%{_datadir}/patriarche/A4-patriarche-*.pdf

%files html
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-html-?.desktop
%{_datadir}/patriarche/patriarche-*.html
%{_datadir}/patriarche/html-1.1/
%{_datadir}/patriarche/html-1.2/
%{_datadir}/patriarche/html-1.3/
%{_datadir}/patriarche/html-2.1/
%{_datadir}/patriarche/index.html

%files txt
%defattr(-,root,root)
%{_datadir}/patriarche/patriarche-*.txt

%files xml
%defattr(-,root,root)
%{_datadir}/patriarche/patriarche-*.xml

%files tools
%defattr(-,root,root)
%{_bindir}/viediff
%{_bindir}/viewdiff
%{_bindir}/viehtml
%{_datadir}/patriarche/vie.dtd
%{_datadir}/patriarche/latex.xsl
%{_datadir}/patriarche/html.xsl
%{_datadir}/patriarche/text.xsl
%{_datadir}/patriarche/Makefile

%files en
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-ps-?-en.desktop
%{_datadir}/patriarche/i18n/en/A4-patriarche-*.ps

%files pdf-en
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-pdf-?-en.desktop
%{_datadir}/patriarche/i18n/en/A4-patriarche-*.pdf

%files html-en
%defattr(-,root,root)
%{_datadir}/patriarche/i18n/en/patriarche-*.html
%{_datadir}/patriarche/i18n/en/html-1.1-en/
%{_datadir}/patriarche/i18n/en/html-1.2-en/
%{_datadir}/patriarche/i18n/en/html-1.3-en/
%{_datadir}/patriarche/i18n/en/html-2.1-en/
%{_datadir}/patriarche/i18n/en/index.html
%{_datadir}/applications/mandriva-%{name}-html-?-en.desktop

%files txt-en
%defattr(-,root,root)
%{_datadir}/patriarche/i18n/en/patriarche-*.txt

%files xml-en
%defattr(-,root,root)
%{_datadir}/patriarche/i18n/en/patriarche-*-en.xml

