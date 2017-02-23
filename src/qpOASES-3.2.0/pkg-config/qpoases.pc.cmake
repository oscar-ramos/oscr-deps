prefix=@CMAKE_INSTALL_PREFIX@
libdir=@CMAKE_INSTALL_PREFIX@/lib
includedir=@CMAKE_INSTALL_PREFIX@/include

Name: qpOASES
Description: qpOASES
URL: https://projects.coin-or.org/qpOASES/
Version: @PACKAGE_VERSION@
Requires:
Conflicts:
Libs: -L${libdir} -lqpOASES
Libs.private:
Cflags: -I${includedir}
