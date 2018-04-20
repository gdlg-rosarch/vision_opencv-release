# Script generated with Bloom
pkgdesc="ROS - `image_geometry` contains C++ and Python libraries for interpreting images geometrically. It interfaces the calibration parameters in sensor_msgs/CameraInfo messages with OpenCV functions such as image rectification, much as cv_bridge interfaces ROS sensor_msgs/Image with OpenCV data types."
url='http://www.ros.org/wiki/image_geometry'

pkgname='ros-lunar-image-geometry'
pkgver='1.12.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.68'
'ros-lunar-opencv3'
'ros-lunar-sensor-msgs'
)

depends=('ros-lunar-opencv3'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=image_geometry
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_geometry $srcdir/image_geometry
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

