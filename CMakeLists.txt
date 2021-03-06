cmake_minimum_required (VERSION 3.5)
project (iib-stats-writer-statsd CXX)

include(conanbuildinfo.cmake)
conan_basic_setup()

include_directories (${CONAN_INCLUDE_DIRS_BOOST})

if (NOT IS_DIRECTORY ${IIB_INSTALL_DIR})
  message (FATAL_ERROR "You must set the IIB_INSTALL_DIR variable!")
endif ()
set (IIB_INCLUDES_DIR ${IIB_INSTALL_DIR}/server/include/plugin)
if (NOT IS_DIRECTORY ${IIB_INCLUDES_DIR})
  message (FATAL_ERROR "The directory ${IIB_INCLUDES_DIR} does not exist!")
endif ()
set (IIB_LIBRARIES_DIR ${IIB_INSTALL_DIR}/server/lib)
if (NOT IS_DIRECTORY ${IIB_LIBRARIES_DIR})
  message (FATAL_ERROR "The directory ${IIB_LIBRARIES_DIR} does not exist!")
endif ()

add_definitions (-DBIP_CXX11_SUPPORT=1)
include_directories (${IIB_INCLUDES_DIR})
find_library (IMBDFPLG NAMES imbdfplg PATHS ${IIB_LIBRARIES_DIR})

add_library (statsdsw SHARED StatsdStatsWriter.cpp StatsdStatsWriter.hpp UdpSocket.cpp UdpSocket.hpp)
target_link_libraries (statsdsw ${IMBDFPLG} ${CONAN_LIBS_BOOST})
set_target_properties (statsdsw PROPERTIES PREFIX "" SUFFIX ".lil" CXX_STANDARD 11)

if (WIN32)
  set (CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Zi")
  set (CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /DEBUG /OPT:REF /OPT:ICF")
endif()

if (UNIX)
  enable_testing()
  add_subdirectory(test)
endif()
