Summary:	Password Database Library
Summary(de):	Paßwortdatenbank-Library
Summary(fr):	Bibliothèque de la base de données des mots de passe
Summary(pl):	Biblioteka Danych u u¿ytkownikach
Summary(tr):	Parola veri tabaný arþivi
Name:		pwdb
Version:	0.56
Release:	3
Copyright:	GPL or BSD
Group:		Base
Group(pl):	Bazowe
Source:		ftp://sysadm.sorosis.ro/pub/libpwdb/%{name}-%{version}.tar.gz
Patch:		%{name}-pld.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
pwdb (Password Database Library) allows configurable access to
and management of /etc/passwd, /etc/shadow, and network authentication
systems including NIS and Radius.

%description -l de
pwdb (Paßwort-Datenbank-Library) ermöglicht den konfigurierbaren Zugriff auf
und die Verwaltung von /etc/passwd, /etc/shadow und
Netzwerk-Authentifikations-Systemen einschließlich NIS und Radius.

%description -l fr
pwdb (Password Database Library) permet un accès configurable à (et la
gestion de) /etc/passwd, /etc/shadow ainsi que des systèmes
d'authentification réseau, dont NIS et Radius.

%description -l pl
Pwdb (Password Database Library) zapewnia spójny interfejs dostêpu do
zarz±dzania bazami danych o u¿ytkownikach. Biblioteka zwalnia aplikacje od
konieczno¶ci samodzielnego przetwarzania baz danych, oraz daje
administratorowi mo¿liwo¶æ wyboru czy dane bêd± pochodziæ z /etc/passwd,
/etc/shadow czy baz sieciowych jak NIS lub RADIUS, poprzez prosty plik
konfiguracyjny.

%description -l tr
pwdb, /etc/passwd ve /etc/shadow dosyalarýnýn yönetimine ve eriþimine, NIS
ve Radius içeren sistemlerde að doðrulamasýna izin verir.

%package	devel
Summary:	PWDB header files
Summary(pl):	Pliki nag³ówkowe do PWDB
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl
Pliki nag³ówkowe do PWDB do tworzenia aplikacji opartych o PWDB.

%package static
Summary:	PWDB static libraries
Summary(pl):	Biblioteki statyczne PWDB
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
PWDB static libraries.

%description static -l pl
Biblioteki statyczne PWDB.

%prep
%setup -c -q
%patch -p1

%build
ln -sf defs/pld.defs default.defs

make OPTIMIZE="$RPM_OPT_FLAGS"

(cd doc; make)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,lib,usr/{include/pwdb,lib}}

make	INCLUDED=$RPM_BUILD_ROOT/usr/include/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/lib \
	install

install conf/pwdb.conf $RPM_BUILD_ROOT/etc/pwdb.conf

mv $RPM_BUILD_ROOT/lib/libp*.a	$RPM_BUILD_ROOT/usr/lib

ln -sf ../../lib/libpwdb.so.*.* \
    $RPM_BUILD_ROOT/usr/lib/libpwdb.so

gzip -9nf doc/pwdb.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/pwdb.txt.bz2 doc/html/*.html
%config %verify(not size mtime md5) /etc/pwdb.conf

%attr(755,root,root) /lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/*.so

/usr/include/pwdb

%files static
%attr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Sun Jan 24 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.55-3d]
- fixed symlinks ... 

* Sat Jan 23 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.55-2d]
- added Group(pl),  
- fixed static subpackage,
- compressed %doc,
- added pld.defines.

* Sun Oct  4 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.55-1d]
- added devel and static subpackages.

%changelog
* Thu Oct 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.54-8d]
- build against Tornado,
- fixed pl translation,
- added %defattr support,
- minor modifications of the spec file.

* Wed Sep 30 1998 Grzegorz Stanis³awski <stangrze@open.net.pl>
- Added Polish translation
- Added BuildRoot

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Mar 13 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to fix a group lookup on the posix compatibility routines

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- added RPM_OPT_FLAGS support
- optimization on a sparc breaks things :-(

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Michael K. Johnson <johnsonm@redhat.com>
- 0.54-3: Updated default config file to work better with shadow, and
          to work with NIS.

* Sat Apr 19 1997 Michael K. Johnson <johnsonm@redhat.com>
- 0.54-2: Included Andrew's patch for long usernames.
