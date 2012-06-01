Name:		judy-fk
Version:	1.0.5
Release:	1%{?dist}
Summary:	General purpose dynamic array with fixed-length keys
Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://sourceforge.net/projects/judy/
#Source0:	http://downloads.sf.net/judy/Judy-%{version}.tar.gz
Source0:	judy-fk-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	Judy
BuildRequires:  Judy-devel

%description
Judy is a C library that provides a state-of-the-art core technology that
implements a sparse dynamic array. Judy arrays are declared simply with a null
pointer. A Judy array consumes memory only when it is populated, yet can grow
to take advantage of all available memory if desired. Judy's key benefits are
scalability, high performance, and memory efficiency. A Judy array is
extensible and can scale up to a very large number of elements, bounded only by
machine memory. Since Judy is designed as an unbounded array, the size of a
Judy array is not pre-allocated but grows and shrinks dynamically with the
array population. This package adds a modified SL library that accepts fixed
length byte arrays.

%package devel
Summary:	Development libraries and headers for Judy SL fixed-key
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development libraries and header files
for developing applications that use the Judy library with fixed keys.

%prep
%setup -q -n judy-fk-%{version}

%build
%configure --disable-static
make 
#%{?_smp_mflags}
# fails to compile properly with parallel make:
# http://sourceforge.net/tracker/index.php?func=detail&aid=2129019&group_id=55753&atid=478138

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
# get rid of static libs and libtool archives
rm -f %{buildroot}%{_libdir}/*.la
# clean out zero length and generated files from doc tree
rm -rf doc/man
rm -f doc/Makefile* doc/ext/README_deliver
[ -s doc/ext/COPYRIGHT ] || rm -f doc/ext/COPYRIGHT
[ -s doc/ext/LICENSE ] || rm -f doc/ext/LICENSE

%check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libjudyfk.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/JudySLFK.h
%{_libdir}/libjudyfk.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed May 30 2010 Miroslav Spousta <miroslav.spousta@gooddata.com> 1.0.5-1
- release
