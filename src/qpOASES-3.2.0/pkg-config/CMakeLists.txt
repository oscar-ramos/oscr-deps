# Set pkg-config for qpOASES
CONFIGURE_FILE (
  ${CMAKE_SOURCE_DIR}/pkg-config/qpoases.pc.cmake
  ${CMAKE_BINARY_DIR}/qpoases.pc @ONLY
  )
# Install pkg-config file
INSTALL (
  FILES  ${CMAKE_BINARY_DIR}/qpoases.pc
  DESTINATION lib/pkgconfig
  )
