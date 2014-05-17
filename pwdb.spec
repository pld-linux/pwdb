Summary:	Password Database Library
Summary(de.UTF-8):	Passwortdatenbank-Library
Summary(fr.UTF-8):	Bibliothèque de la base de données des mots de passe
Summary(pl.UTF-8):	Biblioteka danych o użytkownikach
Summary(tr.UTF-8):	Parola veri tabanı arşivi
Name:		pwdb
Version:	0.62
Release:	2
License:	BSD or GPL
Group:		Base
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/compat-pwdb/pwdb-0.62.tar.gz/1a1fd0312040ef37aa741d09465774b4/%{name}-%{version}.tar.gz
# Source0-md5:	1a1fd0312040ef37aa741d09465774b4
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
aplikacje z konieczności samodzielnego przetwarzania baz danych oraz
daje administratorowi możliwość wyboru poprzez prosty plik
konfiguracyjny, czy dane będą pochodzić z /etc/passwd, /etc/shadow czy
baz sieciowych, takich jak NIS lub RADIUS.

%description -l tr.UTF-8
pwdb, /etc/passwd ve /etc/shadow dosyalarının yönetimine ve erişimine,
NIS ve Radius içeren sistemlerde ağ doğrulamasına izin verir.

%package devel
Summary:	PWDB header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PWDB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PWDB, przeznaczone do tworzenia aplikacji
opartych na PWDB.

%package static
Summary:	PWDB static library
Summary(pl.UTF-8):	Biblioteka statyczna PWDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PWDB static library.

%description static -l pl.UTF-8
Biblioteka statyczna PWDB.

%prep
%setup -q
%patch0 -p1

%build
ln -sf defs/pld.defs default.defs

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib},%{_includedir}/pwdb,%{_libdir}}

%{__make} install \
	INCLUDED=$RPM_BUILD_ROOT%{_includedir}/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/%{_lib}

cp -p conf/pwdb.conf $RPM_BUILD_ROOT%{_sysconfdir}/pwdb.conf

mv -f $RPM_BUILD_ROOT/%{_lib}/libpwdb.a $RPM_BUILD_ROOT%{_libdir}

%{__rm} $RPM_BUILD_ROOT/%{_lib}/libpwdb.so
ln -sf /%{_lib}/libpwdb.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpwdb.so
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS Copyright README doc/pwdb.txt doc/html/*.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pwdb.conf
%attr(755,root,root) /%{_lib}/libpwdb.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libpwdb.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpwdb.so
%{_includedir}/pwdb

%files static
%defattr(644,root,root,755)
%{_libdir}/libpwdb.a
