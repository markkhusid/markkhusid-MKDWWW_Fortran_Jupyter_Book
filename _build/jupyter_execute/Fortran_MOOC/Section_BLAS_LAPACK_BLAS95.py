#!/usr/bin/env python
# coding: utf-8
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# # Section: BLAS/LAPACK - BLAS95
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack)

# ## This program demonstrates the BLAS95 linear algebra library in Fortran.

# ### sdot.f90

# ```fortran
# module sdot_mod
# 
#       public :: sdot
# 
# contains
# 
#       REAL FUNCTION SDOT(N,SX,INCX,SY,INCY)
# !  ====== UPDATE TO DOCUMENTATION ======
# !  To make this calling program compile, I took sdot.f90 for BLAS at
# !  https://netlib.org/blas/ and changed it into a module.
# !  I was not able to get the Intel MKL library to work and the Intel
# !  source code was not available.
# 
# !  =========== DOCUMENTATION ===========
# !
# !* Online html documentation available at
# !            http://www.netlib.org/lapack/explore-html/
# !
# !  Definition:
# !  ===========
# !
# !       REAL FUNCTION SDOT(N,SX,INCX,SY,INCY)
# !
# !       .. Scalar Arguments ..
# !       INTEGER INCX,INCY,N
# !       ..
# !       .. Array Arguments ..
# !       REAL SX(*),SY(*)
# !       ..
# !
# !
# !*> \par Purpose:
# !  =============
# !>
# !*> \verbatim
# !*>
# !*>    SDOT forms the dot product of two vectors.
# !*>    uses unrolled loops for increments equal to one.
# !*> \endverbatim
# !*
# !*  Arguments:
# !*  ==========
# !*
# !*> \param[in] N
# !*> \verbatim
# !*>          N is INTEGER
# !*>         number of elements in input vector(s)
# !*> \endverbatim
# !*>
# !*> \param[in] SX
# !*> \verbatim
# !*>          SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )
# !*> \endverbatim
# !*>
# !*> \param[in] INCX
# !*> \verbatim
# !*>          INCX is INTEGER
# !*>         storage spacing between elements of SX
# !*> \endverbatim
# !*>
# !*> \param[in] SY
# !*> \verbatim
# !*>          SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )
# !*> \endverbatim
# !*>
# !*> \param[in] INCY
# !*> \verbatim
# !*>          INCY is INTEGER
# !*>         storage spacing between elements of SY
# !*> \endverbatim
# !*
# !*  Authors:
# !*  ========
# !*
# !*> \author Univ. of Tennessee
# !*> \author Univ. of California Berkeley
# !*> \author Univ. of Colorado Denver
# !*> \author NAG Ltd.
# !*
# !*> \ingroup single_blas_level1
# !*
# !*> \par Further Details:
# !*  =====================
# !*>
# !*> \verbatim
# !*>
# !*>     jack dongarra, linpack, 3/11/78.
# !*>     modified 12/3/93, array(1) declarations changed to array(*)
# !*> \endverbatim
# !*>
# !*  =====================================================================
# 
# !*
# !*  -- Reference BLAS level1 routine --
# !*  -- Reference BLAS is a software package provided by Univ. of Tennessee,    --
# !*  -- Univ. of California Berkeley, Univ. of Colorado Denver and NAG Ltd..--
# !*
# !*     .. Scalar Arguments ..
#       INTEGER INCX,INCY,N
# !*     ..
# !*     .. Array Arguments ..
#       REAL SX(*),SY(*)
# !*     ..
# !*
# !*  =====================================================================
# !*
# !*     .. Local Scalars ..
#       REAL STEMP
#       INTEGER I,IX,IY,M,MP1
# !*     ..
# !*     .. Intrinsic Functions ..
#       INTRINSIC MOD
# !*     ..
#       STEMP = 0.0e0
#       SDOT = 0.0e0
#       IF (N.LE.0) RETURN
#       IF (INCX.EQ.1 .AND. INCY.EQ.1) THEN
# !*
# !*        code for both increments equal to 1
# !*
# !*
# !*        clean-up loop
# !*
#          M = MOD(N,5)
#          IF (M.NE.0) THEN
#             DO I = 1,M
#                STEMP = STEMP + SX(I)*SY(I)
#             END DO
#             IF (N.LT.5) THEN
#                SDOT=STEMP
#             RETURN
#             END IF
#          END IF
#          MP1 = M + 1
#          DO I = MP1,N,5
#             STEMP = STEMP + SX(I)*SY(I) + SX(I+1)*SY(I+1) + &
#             SX(I+2)*SY(I+2) + SX(I+3)*SY(I+3) + SX(I+4)*SY(I+4)
#          END DO
#       ELSE
# !*
# !*        code for unequal increments or equal increments
# !*          not equal to 1
# !*
#          IX = 1
#          IY = 1
#          IF (INCX.LT.0) IX = (-N+1)*INCX + 1
#          IF (INCY.LT.0) IY = (-N+1)*INCY + 1
#          DO I = 1,N
#             STEMP = STEMP + SX(IX)*SY(IY)
#             IX = IX + INCX
#             IY = IY + INCY
#          END DO
#       END IF
#       SDOT = STEMP
#       RETURN
# !*
# !*     End of SDOT
# !*
#       end function sdot
#       
# end module sdot_mod
# ```
# 

# ### section_blas_lapack_blas95_dot_blas95.f90

# ```fortran
# program dot_test
#     use :: sdot_mod
#     implicit none
#     integer, parameter :: v_size = 5
#     integer :: i
#     real, dimension(v_size) :: vector1 = [ (0.5*I, i=1, v_size) ], &
#                                vector2 = [ (0.1*i, i=1, v_size) ]
#     real, dimension(v_size, v_size) :: matrix = reshape( &
#         [ (real(i), i=1, v_size*v_size) ], [ v_size, v_size ] &
#     )
#     
#     print '(A25, *(F5.1))', 'vector 1: ', vector1
#     print '(A25, *(F5.1))', 'vector 2: ', vector2
#     print '(A25, F6.2)', 'vector 1 . vector 2 =', &
#         sdot(v_size, vector1, 1, vector2, 1)
# 
#     print *
# 
#     print '(A)', 'matrix:'
#     do i = 1, size(matrix, 1)
#         print '(*(F5.1))', matrix(i, :)
#     end do
# 
#     print *
# 
#     print '(A, F6.1)', 'col 2 . col 4:', &
#         sdot(v_size, matrix(:, 2), 1, matrix(:, 4), 1)
# 
#     print *
# 
#     print '(A, F6.1)', 'row 2 . row 4:', &
#         sdot(v_size, matrix(2, :), 1, matrix(4, :), 1)
# 
#     print *
# end program dot_test
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_BLAS_LAPACK_BLAS95"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', "%%section_blas_lapack_blas95_dot_blas95.f90\nprogram dot_test\n    use :: sdot_mod\n    implicit none\n    integer, parameter :: v_size = 5\n    integer :: i\n    real, dimension(v_size) :: vector1 = [ (0.5*I, i=1, v_size) ], &\n                               vector2 = [ (0.1*i, i=1, v_size) ]\n    real, dimension(v_size, v_size) :: matrix = reshape( &\n        [ (real(i), i=1, v_size*v_size) ], [ v_size, v_size ] &\n    )\n    \n    print '(A25, *(F5.1))', 'vector 1: ', vector1\n    print '(A25, *(F5.1))', 'vector 2: ', vector2\n    print '(A25, F6.2)', 'vector 1 . vector 2 =', &\n        sdot(v_size, vector1, 1, vector2, 1)\n\n    print *\n\n    print '(A)', 'matrix:'\n    do i = 1, size(matrix, 1)\n        print '(*(F5.1))', matrix(i, :)\n    end do\n\n    print *\n\n    print '(A, F6.1)', 'col 2 . col 4:', &\n        sdot(v_size, matrix(:, 2), 1, matrix(:, 4), 1)\n\n    print *\n\n    print '(A, F6.1)', 'row 2 . row 4:', &\n        sdot(v_size, matrix(2, :), 1, matrix(4, :), 1)\n\n    print *\nend program dot_test")


# In[6]:


get_ipython().system('bat *.f90')


# In[7]:


os.chdir(code_dir)


# In[8]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# The program is run and the output is saved into a data file *data.dat*.

# In[9]:


exec_status = os.system("fpm run 2>/dev/null")

