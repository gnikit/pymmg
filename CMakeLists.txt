cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(mmg LANGUAGES C CXX)

include(GNUInstallDirs)
include(FetchContent)
include(ExternalProject)

ExternalProject_Add(
  mmg_src
  SOURCE_DIR "${CMAKE_BINARY_DIR}/mmg"
  GIT_REPOSITORY https://github.com/MmgTools/mmg
  GIT_TAG "v5.7.1"
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} -DDEF_MMG5_INT=int64_t
)

# ExternalProject_Get_Property(mmg_src binary_dir)
add_executable(mmg2d_exe IMPORTED GLOBAL)
add_dependencies(mmg2d_exe mmg_src)
add_executable(mmg3d_exe IMPORTED GLOBAL)
add_dependencies(mmg3d_exe mmg_src)
add_executable(mmgs_exe IMPORTED GLOBAL)
add_dependencies(mmgs_exe mmg_src)

if(WIN32)
  set(MMG2D_NAME ${CMAKE_BINARY_DIR}/bin/mmg2d.exe)
  set(MMG3D_NAME ${CMAKE_BINARY_DIR}/bin/mmg3d.exe)
  set(MMGS_NAME ${CMAKE_BINARY_DIR}/bin/mmgs.exe)
else()
  set(MMG2D_NAME ${CMAKE_BINARY_DIR}/bin/mmg2d_O3)
  set(MMG3D_NAME ${CMAKE_BINARY_DIR}/bin/mmg3d_O3)
  set(MMGS_NAME ${CMAKE_BINARY_DIR}/bin/mmgs_O3)
endif()

set_target_properties(mmg2d_exe
  PROPERTIES
  IMPORTED_LOCATION ${MMG2D_NAME}
)
set_target_properties(mmg3d_exe
  PROPERTIES
  IMPORTED_LOCATION ${MMG3D_NAME}
)
set_target_properties(mmgs_exe
  PROPERTIES
  IMPORTED_LOCATION ${MMGS_NAME}
)

install(IMPORTED_RUNTIME_ARTIFACTS mmgs_exe
  RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/src/mmgs
)
install(IMPORTED_RUNTIME_ARTIFACTS mmg2d_exe
  RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/src/mmg2d
)
install(IMPORTED_RUNTIME_ARTIFACTS mmg3d_exe
  RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/src/mmg3d
)