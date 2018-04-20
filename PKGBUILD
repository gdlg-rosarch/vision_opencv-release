# Script generated with Bloom
pkgdesc="ROS - This contains CvBridge, which converts between ROS Image messages and OpenCV images."
url='http://www.ros.org/wiki/cv_bridge'

pkgname='ros-lunar-cv-bridge'
pkgver='1.12.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'python2'
'python2-numpy'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-opencv3>=3.3.0'
'ros-lunar-rosconsole'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
)

depends=('boost'
'python2'
'ros-lunar-opencv3>=3.3.0'
'ros-lunar-rosconsole'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=cv_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/cv_bridge $srcdir/cv_bridge
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

