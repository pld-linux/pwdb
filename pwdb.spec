Summary:	Password Database Library
Summary(de.UTF-8):	Passwortdatenbank-Library
Summary(fr.UTF-8):	Bibliothèque de la base de données des mots de passe
Summary(pl.UTF-8):	Biblioteka Danych o użytkownikach
Summary(tr.UTF-8):	Parola veri tabanı arşivi
Name:		pwdb
Version:	0.61
Release:	6
License:	GPL/BSD
Group:		Base
Source0:	ftp://sysadm.sorosis.ro/pub/libpwdb/%{name}-%{version}.tar.gz
# Source0-md5:	47e2dc0d5590390fe7a3937961575b09
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

%description -l de.UTF-8
Das pwdb-Paket enthält libpwdb, die Passwortdatenbank-Library. Libpwdb
ist eine Library, die eine Userinformations-Datenbank implementiert,
und mit Linux-PAM (Pluggable Authentication Modules) zusammenarbeited.
Libpwdb erlaubt konfigurierbaren Zugriff auf /etc/passwd, /etc/shadow
und Netzwerkauthentifizierungssysteme wie NIS und Radius.

%description -l fr.UTF-8
pwdb (Password Database Library) permet un accès configurable à (et la
gestion de) /etc/passwd, /etc/shadow ainsi que des systèmes
d'authentification réseau, dont NIS et Radius.

%description -l pl.UTF-8
Pwdb (Password Database Library) zapewnia spójny interfejs dostępu do
zarządzania bazami danych o użytkownikach. Biblioteka zwalnia
aplikacje od konieczności samodzielnego przetwarzania baz danych, oraz
daje administratorowi możliwość wyboru czy dane będą pochodzić z
/etc/passwd, /etc/shadow czy baz sieciowych jak NIS lub RADIUS,
poprzez prosty plik konfiguracyjny.

%description -l tr.UTF-8
pwdb, /etc/passwd ve /etc/shadow dosyalarının yönetimine ve erişimine,
NIS ve Radius içeren sistemlerde ağ doğrulamasına izin verir.

%package devel
Summary:	PWDB header files
Summary(pl.UTF-8):	Pliki nagłówkowe do PWDB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do PWDB do tworzenia aplikacji opartych o PWDB.

%package static
Summary:	PWDB static libraries
Summary(pl.UTF-8):	Biblioteki statyczne PWDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PWDB static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne PWDB.

%prep
%setup -c -q
%patch0 -p1

%build
ln -sf defs/pld.defs default.defs

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib},%{_includedir}/pwdb,%{_libdir}}

%{__make} install \
	INCLUDED=$RPM_BUILD_ROOT%{_includedir}/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/%{_lib}

install conf/pwdb.conf $RPM_BUILD_ROOT%{_sysconfdir}/pwdb.conf

mv -f $RPM_BUILD_ROOT/%{_lib}/libp*.a	$RPM_BUILD_ROOT%{_libdir}

ln -sf /%{_lib}/libpwdb.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpwdb.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/pwdb.txt doc/html/*.html
%config %verify(not md5 mtime size) %{_sysconfdir}/pwdb.conf
%attr(755,root,root) /%{_lib}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/pwdb

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
