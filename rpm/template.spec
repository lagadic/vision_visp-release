Name:           ros-jade-visp-bridge
Version:        0.10.0
Release:        0%{?dist}
Summary:        ROS visp_bridge package

Group:          Development/Libraries
License:        GPLv2
URL:            http://wiki.ros.org/visp_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-camera-calibration-parsers
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-visp
BuildRequires:  ros-jade-camera-calibration-parsers
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-visp

%description
Converts between ROS structures and ViSP structures.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Feb 13 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.10.0-0
- Autogenerated by Bloom

* Mon Dec 21 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.9.1-0
- Autogenerated by Bloom

* Sun Dec 20 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.9.0-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.8.0-0
- Autogenerated by Bloom

