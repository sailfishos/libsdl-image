%undefine __cmake_in_source_build

Summary: Simple DirectMedia Layer - Sample Image Loading Library
Name: SDL2_image
Version: 2.8.2
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libsdl-org/SDL_image
License: zlib
BuildRequires: cmake
BuildRequires: pkgconfig(sdl2)
BuildRequires: libjpeg-turbo-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package devel
Summary: Simple DirectMedia Layer - Sample Image Loading Library (Development)
Requires: %{name}

%description devel
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*
