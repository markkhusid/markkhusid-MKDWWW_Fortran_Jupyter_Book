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
# # Section Arrays: Array Timing

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates the different computation times on 2x2 matrices using various Fortran techniques.

# ```fortran
# program array_timings
#     use, intrinsic :: iso_fortran_env, only : DP => REAL64, error_unit
#     implicit none
#     integer, parameter :: nr_rows = 10000, nr_cols = 10000
#     real(kind=DP), parameter :: delta = 1e-7_DP
#     real(kind=DP), dimension(:, :), allocatable :: A, B, C, A_old
#     real :: start_time, end_time
#     integer :: istat, row, col
# 
#     ! allocate arrays
#     allocate (A(nr_rows, nr_cols), B(nr_rows, nr_cols), C(nr_rows, nr_cols), &
#               A_old(nr_rows, nr_cols), stat=istat)
#     if (istat /= 0) then
#         write (unit=error_unit, fmt='(A)') 'error: can not allocated arrays'
#         stop 1
#     end if
# 
#     ! initialize arrays
#     call random_number(B)
#     call random_number(C)
# 
#     ! compute array expressions
#     call cpu_time(start_time)
#     A = 5.0_DP*B + sqrt(2.5_DP*C)/3.2_DP
#     call cpu_time(end_time)
#     print '(A, F12.6)', 'array expression: ', end_time - start_time
# 
#     ! store result for comparison
#     A_old = A
# 
#     ! compute do loops
#     call cpu_time(start_time)
#     do col = 1, nr_cols
#         do row = 1, nr_rows
#             A(row, col) = 5.0_DP*B(row, col) + sqrt(2.5_DP*C(row, col))/3.2_DP
#         end do
#     end do
#     call cpu_time(end_time)
#     print '(A, F12.6)', 'do loops: ', end_time - start_time
# 
#     ! check result
#     if (.not. are_almost_equal(A, A_old, delta)) &
#         print '(A, E7.2)', 'warning: not equal up to ', delta
# 
#     ! compute forall
#     call cpu_time(start_time)
#     forall (row = 1:nr_rows, col=1:nr_cols)
#         A(row, col) = 5.0_DP*B(row, col) + sqrt(2.5_DP*C(row, col))/3.2_DP
#     end forall
#     call cpu_time(end_time)
#     print '(A, F12.6)', 'forall: ', end_time - start_time
# 
#     ! check result
#     if (.not. are_almost_equal(A, A_old, delta)) &
#         print '(A, E7.2)', 'warning: not equal up to ', delta
# 
#     ! compute do concurrent
#     call cpu_time(start_time)
#     do concurrent (row = 1:nr_rows, col=1:nr_cols)
#         A(row, col) = 5.0_DP*B(row, col) + sqrt(2.5_DP*C(row, col))/3.2_DP
#         end do
#     call cpu_time(end_time)
#     print '(A, F12.6)', 'do concurrent: ', end_time - start_time
# 
#     ! check result
#     if (.not. are_almost_equal(A, A_old, delta)) &
#         print '(A, E7.2)', 'warning: not equal up to ', delta
#     ! deallocate arrays
#     deallocate(A, B, C, A_old)
#     
# contains
# 
#     function are_almost_equal(A, B, delta) result(are_same)
#         implicit none
#         real(kind=DP), dimension(:, :), intent(in) :: A, B
#         real(kind=DP), value :: delta
#         logical :: are_same
# 
#         are_same = all(abs(A - B)/A < delta)
#     end function are_almost_equal
# 
# end program array_timings
# 
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Array_Timing"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

