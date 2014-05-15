Name:           judy-fk
Version:        1.0.6
Release:        1%{?dist}
Summary:        General purpose dynamic array with fixed-length keys

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://github.com/qiq/judy-fk/
Source0:        https://github.com/qiq/judy-fk/releases/download/v%{version}/judy-fk-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

%package        devel
Summary:        Development files for Judy SL fixed-key
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu May 15 2014 Miroslav Spousta <miroslav.spousta@gooddata.com> 1.0.6-1
- Copyright and spec file adjustments for Fedora

* Sun May 30 2010 Miroslav Spousta <miroslav.spousta@gooddata.com> 1.0.5-1
- release
