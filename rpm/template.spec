Name:           ros-lunar-visp-tracker
Version:        0.10.0
Release:        1%{?dist}
Summary:        ROS visp_tracker package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/wiki/visp_tracker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-image-proc
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-message-generation
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-resource-retriever
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
Requires:       ros-lunar-visp
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-image-proc
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-resource-retriever
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-visp

%description
Wraps the ViSP moving edge tracker provided by the ViSP visual servoing library
into a ROS package. This computer vision algorithm computes the pose (i.e.
position and orientation) of an object in an image. It is fast enough to allow
object online tracking using a camera.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Jun 23 2017 Fabien Spindler <fabien.spindler@inria.fr> - 0.10.0-1
- Autogenerated by Bloom

* Fri Jun 23 2017 Fabien Spindler <fabien.spindler@inria.fr> - 0.10.0-0
- Autogenerated by Bloom

