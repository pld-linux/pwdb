Summary:	Password Database Library
Summary(de):	Paßwortdatenbank-Library
Summary(fr):	Bibliothèque de la base de données des mots de passe
Summary(pl):	Biblioteka Danych o u¿ytkownikach
Summary(tr):	Parola veri tabaný arþivi
Name:		pwdb
Version:	0.57
Release:	4
Copyright:	GPL or BSD
Group:		Base
Group(pl):	Podstawowe
Source:		ftp://sysadm.sorosis.ro/pub/libpwdb/%{name}-%{version}.tar.gz
Patch:		pwdb-pld.patch
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
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl
Pliki nag³ówkowe do PWDB do tworzenia aplikacji opartych o PWDB.

%package	static
Summary:	PWDB static libraries
Summary(pl):	Biblioteki statyczne PWDB
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
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

make	INCLUDED=$RPM_BUILD_ROOT%{_includedir}/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/lib \
	install

install conf/pwdb.conf $RPM_BUILD_ROOT/etc/pwdb.conf

mv $RPM_BUILD_ROOT/lib/libp*.a	$RPM_BUILD_ROOT%{_libdir}

ln -sf ../../lib/libpwdb.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpwdb.so

strip --strip-unneeded $RPM_BUILD_ROOT/lib/*.so.*

gzip -9nf doc/pwdb.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/pwdb.txt.gz doc/html/*.html

%config %verify(not size mtime md5) /etc/pwdb.conf

%attr(755,root,root) /lib/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

%{_includedir}/pwdb

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
