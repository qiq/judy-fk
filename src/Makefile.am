AM_CFLAGS = @WARN_CFLAGS@

lib_LTLIBRARIES = libjudyfk.la

include_HEADERS = JudySLFK.h
libjudyfk_la_SOURCES = JudySLFK.h JudySLFK.c
libjudyfk_la_CFLAGS = $(AM_CFLAGS)
libjudyfk_la_LIBADD = -lJudy
libjudyfk_la_LDFLAGS = $(VERSION_INFO) $(AM_LDFLAGS)
