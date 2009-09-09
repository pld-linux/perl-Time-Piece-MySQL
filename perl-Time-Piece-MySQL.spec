#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Piece-MySQL
Summary:	Time::Piece::MySQL - Adds MySQL-specific methods to Time::Piece
Summary(pl.UTF-8):	Time::Piece::MySQL - dodaje specyficzne metody MySQL do Time::Piece
Name:		perl-Time-Piece-MySQL
Version:	0.06
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KASEI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be66a577f8790c16947d8e3e5a0e65a2
URL:		http://search.cpan.org/dist/Time-Piece-MySQL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Using this module instead of, or in addition to, Time::Piece adds a
few MySQL-specific date-time methods to Time::Piece objects.

%description -l pl.UTF-8
Użycie tego modułu zamiast lub razem z Time::Piece dodaje kilka
charakterystycznych dla MySQL metod związanych z datą i czasem do
objektów Time::Piece.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Time/Piece
%{perl_vendorlib}/Time/Piece/*.pm
%{_mandir}/man3/*
