Name:           crystalhd
Summary:        Kernel module (kmod) for crystalhd
Version:        20170515
Release:        2%{?dist}
License:        GPLv2
URL:            https://github.com/philipl/crystalhd.git
#Source0:        crystalhd-%{version}.tar.xz

ExclusiveArch:  i686 x86_64
Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}
Requires:       %{name}-firmware >= 3.10.0
Requires:       libcrystalhd >= 3.10.0
Requires:       unifdef


%description
CrystalHD common files.

%prep
#setup -q -c


%build
#Nothing to build


%install
#Nothing to prep

%files
#doc drivers/staging/crystalhd/TODO

%changelog
* Mon Mar 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 20170515-2
- Add missing unifdef

* Wed May 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 20170515-1
- Update to 20170515

* Wed Jan 15 2014 Nicolas Chauvet <kwizart@gmail.com> - 20131018-2
- Update to 20131018
- Add ExclusiveArch

* Fri Apr 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130426-2
- Add dependencies

* Wed Jan 16 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130106-1
- Initial spec file

