cmake_minimum_required(VERSION 2.8.3)
project(ee_cart_imped_launch)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# TODO: fill in what other packages will need to use this package
catkin_package(
    DEPENDS ee_cart_imped_action ee_cart_imped_control
    CATKIN_DEPENDS # TODO
    INCLUDE_DIRS ${catkin_INCLUDE_DIRS}
    LIBRARIES # TODO
)

# Don't know if I need these last two lines 
#include_directories(${Boost_INCLUDE_DIRS})
#target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
