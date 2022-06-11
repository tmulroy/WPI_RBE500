# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "message_runtime;roscpp;rospy".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lquat_to_euler;-lgeometry_msgs".split(';') if "-lquat_to_euler;-lgeometry_msgs" != "" else []
PROJECT_NAME = "quat_to_euler"
PROJECT_SPACE_DIR = "/home/tom/rbe500-ros/install"
PROJECT_VERSION = "0.0.0"
