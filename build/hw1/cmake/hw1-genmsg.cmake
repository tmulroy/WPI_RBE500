# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "hw1: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ihw1:/home/tom/rbe500-ros/src/hw1/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(hw1_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_custom_target(_hw1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "hw1" "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" ""
)

get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_custom_target(_hw1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "hw1" "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(hw1
  "/home/tom/rbe500-ros/src/hw1/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hw1
)

### Generating Services
_generate_srv_cpp(hw1
  "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hw1
)

### Generating Module File
_generate_module_cpp(hw1
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hw1
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(hw1_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(hw1_generate_messages hw1_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_dependencies(hw1_generate_messages_cpp _hw1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_dependencies(hw1_generate_messages_cpp _hw1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hw1_gencpp)
add_dependencies(hw1_gencpp hw1_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hw1_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(hw1
  "/home/tom/rbe500-ros/src/hw1/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hw1
)

### Generating Services
_generate_srv_eus(hw1
  "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hw1
)

### Generating Module File
_generate_module_eus(hw1
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hw1
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(hw1_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(hw1_generate_messages hw1_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_dependencies(hw1_generate_messages_eus _hw1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_dependencies(hw1_generate_messages_eus _hw1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hw1_geneus)
add_dependencies(hw1_geneus hw1_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hw1_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(hw1
  "/home/tom/rbe500-ros/src/hw1/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hw1
)

### Generating Services
_generate_srv_lisp(hw1
  "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hw1
)

### Generating Module File
_generate_module_lisp(hw1
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hw1
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(hw1_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(hw1_generate_messages hw1_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_dependencies(hw1_generate_messages_lisp _hw1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_dependencies(hw1_generate_messages_lisp _hw1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hw1_genlisp)
add_dependencies(hw1_genlisp hw1_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hw1_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(hw1
  "/home/tom/rbe500-ros/src/hw1/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/hw1
)

### Generating Services
_generate_srv_nodejs(hw1
  "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/hw1
)

### Generating Module File
_generate_module_nodejs(hw1
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/hw1
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(hw1_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(hw1_generate_messages hw1_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_dependencies(hw1_generate_messages_nodejs _hw1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_dependencies(hw1_generate_messages_nodejs _hw1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hw1_gennodejs)
add_dependencies(hw1_gennodejs hw1_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hw1_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(hw1
  "/home/tom/rbe500-ros/src/hw1/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1
)

### Generating Services
_generate_srv_py(hw1
  "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1
)

### Generating Module File
_generate_module_py(hw1
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(hw1_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(hw1_generate_messages hw1_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/msg/Num.msg" NAME_WE)
add_dependencies(hw1_generate_messages_py _hw1_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tom/rbe500-ros/src/hw1/srv/MultiplyTwoNums.srv" NAME_WE)
add_dependencies(hw1_generate_messages_py _hw1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hw1_genpy)
add_dependencies(hw1_genpy hw1_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hw1_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hw1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hw1
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(hw1_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hw1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hw1
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(hw1_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hw1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hw1
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(hw1_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/hw1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/hw1
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(hw1_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hw1
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(hw1_generate_messages_py std_msgs_generate_messages_py)
endif()
