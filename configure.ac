AC_PREREQ(2.57)
AC_INIT(judy-fk, 1.0.6, miroslav.spousta@gooddata.comm)

AC_CONFIG_MACRO_DIR([m4])

AM_MAINTAINER_MODE

dnl Turn on automake, and pass it the PACKAGE_NAME and PACKAGE_VERSION, too.
AM_INIT_AUTOMAKE($PACKAGE_NAME, $PACKAGE_VERSION)

dnl Tell autoconf we want to keep our preprocessor defines in a header named
dnl config.h.  This keeps automake from passing a zillion -D directives to
dnl the C compiler.
AM_CONFIG_HEADER([config.h])

dnl We are keeping the same version info as libJudy
VERSION_INFO="-version-info 1:3:0"
AC_SUBST(VERSION_INFO)

dnl==========================================================================
dnl Checks for Programs
dnl==========================================================================
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET

dnl==========================================================================
dnl Checks for Header Files
dnl==========================================================================
AC_HEADER_STDC
AC_CHECK_HEADERS([string.h])

dnl==========================================================================
dnl Checks for Typedefs, Structures, and Compiler Characteristics
dnl==========================================================================

dnl Standard, boring stuff.
AC_HEADER_STDBOOL
AC_C_CONST
AC_C_INLINE

dnl If we're compiling for a little-endian system, define JU_LITTLE_ENDIAN.
dnl If we can't tell what kind of system we're compling for, alert the
dnl user as described in 'info autoconf'.
AC_C_BIGENDIAN(, AC_DEFINE(JU_LITTLE_ENDIAN, 1,
			   [Define to 1 on little-endian systems.]))

dnl  Figure out if we are 32-bit or 64-bit (LP64)
AC_CHECK_SIZEOF(void *)
if test "$ac_cv_sizeof_void_p" = 8; then 
    AC_MSG_RESULT(Detected 64-bit Build Environment)
    CFLAGS="-DJU_64BIT $CFLAGS"
else 
    AC_MSG_RESULT(Detected 32-bit Build Environment)
      CFLAGS="-UJU_64BIT $CFLAGS"
fi

AC_ARG_ENABLE(32-bit, [  --enable-32-bit          Generate code for a 32-bit environment],
	      b32="$enableval", b32="no")
if test x"$b32" != "xno"; then
    AC_MSG_RESULT(Configured to Build 32-bit)
    if test x"$GCC" = xyes; then
      CFLAGS="-UJU_64BIT -m32 $CFLAGS"
    else
      CFLAGS="-UJU_64BIT $CFLAGS"
    fi
fi

AC_ARG_ENABLE(64-bit, [  --enable-64-bit          Generate code for a 64-bit environment],
              b64="$enableval", b64="no")
if test x"$b64" != "xno"; then
    AC_MSG_RESULT(Configured to Building 64-bit)
    if test x"$GCC" = xyes; then
      CFLAGS="-DJU_64BIT -m64 $CFLAGS"
    else
      CFLAGS="-DJU_64BIT $CFLAGS"
    fi
fi

dnl==========================================================================
dnl Checks for Libraries
dnl==========================================================================

AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_FUNC_MEMCMP
AC_FUNC_MMAP
AC_FUNC_STAT
AC_FUNC_VPRINTF
AC_CHECK_FUNCS([getpagesize gettimeofday memset munmap pow strchr strcspn strerror strstr strtoul uname])

dnl These must be called before AM_PROG_LIBTOOL, because it may want
dnl to call AC_CHECK_PROG.
AC_CHECK_TOOL(AR, ar)
AC_CHECK_TOOL(LD, ld)
AC_CHECK_TOOL(RANLIB, ranlib, :)

dnl Checks for libtool - this must be done after we set cflags (abi issues)
dnl
AM_PROG_LIBTOOL

WARN_CFLAGS=""
build_warnings="-W -Wall -Wstrict-prototypes -Wmissing-prototypes"
AC_ARG_ENABLE([build-warnings],
	      [  --enable-build-warnings    Enable build-time compiler warnings for gcc])
if test x"$build_warnings" = xyes; then
    if test x"$GCC" = xyes; then
	WARN_CFLAGS="${build_warnings}"
    fi
fi

AC_SUBST(WARN_CFLAGS)

AC_CONFIG_FILES([Makefile
                 src/Makefile])


AC_OUTPUT
