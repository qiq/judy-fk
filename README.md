# judy-fk

This is a modified JudySL implementation, so that keys are not NUL-terminated C
strings, but fixed-length sequence of bytes. Except this, it is the same as
original JudySL implementation.

For more info see http://judy.sourceforge.net/

## Getting started

**Clone sources**

```
$ git clone https://github.com/qiq/judy-fk
$ cd judy-fk
```

**Build using CMake**

```
$ mkdir build
$ cd build
$ cmake ..
# -- Configuring done
# -- Generating done
# -- Build files have been written to: /Users/tomaskorcak/dev/gdc-bear/external/judy-fk/build
$ make
# [ 50%] Building C object CMakeFiles/judy-fk.dir/src/JudySLFK.c.o
# [100%] Linking C static library libjudy-fk.a
# [100%] Built target judy-fk
```
