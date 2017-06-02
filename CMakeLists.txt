cmake_minimum_required(VERSION 3.7)

project(judy-fk)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

include_directories(src)

find_package(Judy)
if ( NOT Judy_FOUND )
  message(FATAL_ERROR "Package Judy required, but not found!")
else()
  include_directories(${Judy_INCLUDE_DIRS})
endif( NOT Judy_FOUND )

set(SOURCE
  ${SOURCE}

  src/JudySLFK.c
)

add_library(judy-fk-static STATIC ${SOURCE})
add_library(judy-fk-shared SHARED ${SOURCE})
target_link_libraries(judy-fk-shared ${Judy_LIBRARY})

SET_TARGET_PROPERTIES(judy-fk-static PROPERTIES OUTPUT_NAME judy-fk CLEAN_DIRECT_OUTPUT 1)
SET_TARGET_PROPERTIES(judy-fk-shared PROPERTIES OUTPUT_NAME judy-fk CLEAN_DIRECT_OUTPUT 1)
