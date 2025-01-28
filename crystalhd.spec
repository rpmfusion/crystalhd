Name:           crystalhd
Summary:        Kernel module (kmod) for crystalhd
Version:        20220825
Release:        5%{?dist}
License:        GPLv2
URL:            https://github.com/kwizart/crystalhd.git

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
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20220825-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20220825-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20220825-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20220825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Aug 25 2022 Nicolas Chauvet <kwizart@gmail.com> - 20220825-1
- Update to 20220825

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20170515-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20170515-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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

