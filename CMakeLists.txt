cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(mmg LANGUAGES C CXX)

include(GNUInstallDirs)
include(FetchContent)
include(ExternalProject)

ExternalProject_Add(
  mmg_src
  SOURCE_DIR "${CMAKE_BINARY_DIR}/mmg"
  GIT_REPOSITORY https://github.com/MmgTools/mmg
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} -DDEF_MMG5_INT=int64_t
)

# ExternalProject_Get_Property(mmg_src binary_dir)
add_executable(mmg2d_exe IMPORTED GLOBAL)
add_dependencies(mmg2d_exe mmg_src)
add_executable(mmg3d_exe IMPORTED GLOBAL)
add_dependencies(mmg3d_exe mmg_src)
add_executable(mmgs_exe IMPORTED GLOBAL)
add_dependencies(mmgs_exe mmg_src)

set_target_properties(mmg2d_exe
  PROPERTIES
  IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/bin/mmg2d_O3
)
set_target_properties(mmg3d_exe
  PROPERTIES
  IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/bin/mmg3d_O3
)
set_target_properties(mmgs_exe
  PROPERTIES
  IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/bin/mmgs_O3
)

install(IMPORTED_RUNTIME_ARTIFACTS mmg2d_exe mmg3d_exe mmgs_exe
  DESTINATION ${CMAKE_INSTALL_BINDIR}
)
