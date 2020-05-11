Summary: Simple DirectMedia Layer - Sample Image Loading Library
Name: SDL2_image
Version: 2.0.5
Release: 1
Source: http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_image/
License: zlib
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
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*