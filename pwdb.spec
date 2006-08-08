Summary:	Password Database Library
Summary(de):	Passwortdatenbank-Library
Summary(fr):	Biblioth�que de la base de donn�es des mots de passe
Summary(pl):	Biblioteka Danych o u�ytkownikach
Summary(tr):	Parola veri taban� ar�ivi
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

%description -l de
Das pwdb-Paket enth�lt libpwdb, die Passwortdatenbank-Library. Libpwdb
ist eine Library, die eine Userinformations-Datenbank implementiert,
und mit Linux-PAM (Pluggable Authentication Modules) zusammenarbeited.
Libpwdb erlaubt konfigurierbaren Zugriff auf /etc/passwd, /etc/shadow
und Netzwerkauthentifizierungssysteme wie NIS und Radius.

%description -l fr
pwdb (Password Database Library) permet un acc�s configurable � (et la
gestion de) /etc/passwd, /etc/shadow ainsi que des syst�mes
d'authentification r�seau, dont NIS et Radius.

%description -l pl
Pwdb (Password Database Library) zapewnia sp�jny interfejs dost�pu do
zarz�dzania bazami danych o u�ytkownikach. Biblioteka zwalnia
aplikacje od konieczno�ci samodzielnego przetwarzania baz danych, oraz
daje administratorowi mo�liwo�� wyboru czy dane b�d� pochodzi� z
/etc/passwd, /etc/shadow czy baz sieciowych jak NIS lub RADIUS,
poprzez prosty plik konfiguracyjny.

%description -l tr
pwdb, /etc/passwd ve /etc/shadow dosyalar�n�n y�netimine ve eri�imine,
NIS ve Radius i�eren sistemlerde a� do�rulamas�na izin verir.

%package devel
Summary:	PWDB header files
Summary(pl):	Pliki nag��wkowe do PWDB
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for developing PWDB based applications.

%description devel -l pl
Pliki nag��wkowe do PWDB do tworzenia aplikacji opartych o PWDB.

%package static
Summary:	PWDB static libraries
Summary(pl):	Biblioteki statyczne PWDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PWDB static libraries.

%description static -l pl
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
