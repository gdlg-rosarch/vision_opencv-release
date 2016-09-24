Name:           ros-kinetic-cv-bridge
Version:        1.12.2
Release:        0%{?dist}
Summary:        ROS cv_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/cv_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-devel
Requires:       ros-kinetic-opencv3
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  python-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-opencv3
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs

%description
This contains CvBridge, which converts between ROS Image messages and OpenCV
images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Sep 24 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.0-1
- Autogenerated by Bloom

* Fri Mar 18 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

