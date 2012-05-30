#ifndef _JUDY_SLFK_INCLUDED
#define _JUDY_SLFK_INCLUDED
// _________________
//
// Copyright (C) 2000 - 2002 Hewlett-Packard Company
//
// This program is free software; you can redistribute it and/or modify it
// under the term of the GNU Lesser General Public License as published by the
// Free Software Foundation; either version 2 of the License, or (at your
// option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
// for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program; if not, write to the Free Software Foundation,
// Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
// _________________

// @(#) $Revision: 4.52 $ $Source: /judy/src/Judy.h $
//
// HEADER FILE FOR EXPORTED FEATURES IN JUDY LIBRARY, libJudy.*
//
// See the manual entries for details.
//
// Note:  This header file uses old-style comments on #-directive lines and
// avoids "()" on macro names in comments for compatibility with older cc -Aa
// and some tools on some platforms.


#include <Judy.h>

#ifdef __cplusplus      /* support use by C++ code */
extern "C" {
#endif

// ****************************************************************************
// JUDYSL FUNCTIONS:

extern PPvoid_t JudySLFKGet(       Pcvoid_t, const uint8_t * Index, Word_t len, P_JE);
extern PPvoid_t JudySLFKIns(       PPvoid_t, const uint8_t * Index, Word_t len, P_JE);
extern int      JudySLFKDel(       PPvoid_t, const uint8_t * Index, Word_t len, P_JE);
extern Word_t   JudySLFKFreeArray( PPvoid_t,                        Word_t len, P_JE);
extern PPvoid_t JudySLFKFirst(     Pcvoid_t,       uint8_t * Index, Word_t len, P_JE);
extern PPvoid_t JudySLFKNext(      Pcvoid_t,       uint8_t * Index, Word_t len, P_JE);
extern PPvoid_t JudySLFKLast(      Pcvoid_t,       uint8_t * Index, Word_t len, P_JE);
extern PPvoid_t JudySLFKPrev(      Pcvoid_t,       uint8_t * Index, Word_t len, P_JE);

// Some of the macros are special cases that use inlined shortcuts for speed
// with root-level leaves:

// This is a slower version with current processors, but in the future...

#define JSLGFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV,    PArray,   Index, Len, JudySLFKGet,   "JudySLFKGet")
#define JSLIFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV, (&(PArray)), Index, Len, JudySLFKIns,   "JudySLFKIns")
#define JSLDFK( Rc,    PArray,   Index, Len)                                   \
        J_2I( Rc, (&(PArray)), Index, Len, JudySLFKDel,   "JudySLFKDel")
#define JSLFFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV,    PArray,   Index, Len, JudySLFKFirst, "JudySLFKFirst")
#define JSLNFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV,    PArray,   Index, Len, JudySLFKNext,  "JudySLFKNext")
#define JSLLFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV,    PArray,   Index, Len, JudySLFKLast,  "JudySLFKLast")
#define JSLPFK( PV,    PArray,   Index, Len)                                   \
        J_2P( PV,    PArray,   Index, Len, JudySLFKPrev,  "JudySLFKPrev")
#define JSLFAFK(Rc,    PArray, Len)                                            \
        J_1I( Rc, (&(PArray)), Len, JudySLFKFreeArray, "JudySLFKFreeArray")

#ifdef __cplusplus
}
#endif
#endif /* ! _JUDY_SLFK_INCLUDED */
