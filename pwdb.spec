Summary:	Password Database Library
Summary(de):	Passwortdatenbank-Library
Summary(fr):	BibliothËque de la base de donnÈes des mots de passe
Summary(pl):	Biblioteka Danych o uøytkownikach
Summary(tr):	Parola veri taban˝ ar˛ivi
Name:		pwdb
Version:	0.61
Release:	1
License:	GPL or BSD
Group:		Base
Group(de):	Gr¸nds‰tzlich
Group(pl):	Podstawowe
Source0:	ftp://sysadm.sorosis.ro/pub/libpwdb/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pwdb package contains libpwdb, the password database library.
Libpwdb is a library which implements a generic user information
database. Libpwdb was specifically designed to work with Linux's PAM
(Pluggable Authentication Modules). Libpwdb allows configurable access
to and management of security tools like /etc/passwd, /etc/shadow and
network authentication systems including NIS and Radius.

%description -l de
Das pwdb-Paket enth‰lt libpwdb, die Passwortdatenbank-Library. Libpwdb
ist eine Library, die eine Userinformations-Datenbank implementiert,
und mit Linux-PAM (Pluggable Authentication Modules) zusammenarbeited.
Libpwdb erlaubt konfigurierbaren Zugriff auf /etc/passwd, /etc/shadow
und Netzwerkauthentifizierungssysteme wie NIS und Radius.

%description -l fr
pwdb (Password Database Library) permet un accËs configurable ‡ (et la
gestion de) /etc/passwd, /etc/shadow ainsi que des systËmes
d'authentification rÈseau, dont NIS et Radius.

%description -l pl
Pwdb (Password Database Library) zapewnia spÛjny interfejs dostÍpu do
zarz±dzania bazami danych o uøytkownikach. Biblioteka zwalnia
aplikacje od konieczno∂ci samodzielnego przetwarzania baz danych, oraz
daje administratorowi moøliwo∂Ê wyboru czy dane bÍd± pochodziÊ z
/etc/passwd, /etc/shadow czy baz sieciowych jak NIS lub RADIUS,
poprzez prosty plik konfiguracyjny.

%description -l tr
pwdb, /etc/passwd ve /etc/shadow dosyalar˝n˝n yˆnetimine ve eri˛imine,
NIS ve Radius iÁeren sistemlerde a dorulamas˝na izin verir.

%package devel
Summary:	PWDB header files
Summary(pl):	Pliki nag≥Ûwkowe do PWDB
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl
Pliki nag≥Ûwkowe do PWDB do tworzenia aplikacji opartych o PWDB.

%package static
Summary:	PWDB static libraries
Summary(pl):	Biblioteki statyczne PWDB
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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

%{__make} OPTIMIZE="%{rpmcflags}"

(cd doc; %{__make})

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,lib,usr/{include/pwdb,lib}}

%{__make} install \
	INCLUDED=$RPM_BUILD_ROOT%{_includedir}/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/lib

install conf/pwdb.conf $RPM_BUILD_ROOT%{_sysconfdir}/pwdb.conf

mv -f $RPM_BUILD_ROOT/lib/libp*.a	$RPM_BUILD_ROOT%{_libdir}

ln -sf ../../lib/libpwdb.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpwdb.so

gzip -9nf doc/pwdb.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/pwdb.txt.gz doc/html/*.html
%config %verify(not size mtime md5) %{_sysconfdir}/pwdb.conf
%attr(755,root,root) /lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/pwdb

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
