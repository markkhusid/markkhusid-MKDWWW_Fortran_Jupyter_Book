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
# # Section Arrays: Normalize Performance
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program tests the performance of various methods of performing matrix normalization in Fortran.

# ```fortran
# program normalize_performance
#     use, intrinsic :: iso_fortran_env, only : error_unit, DP => REAL64
#     implicit none
#     integer :: matrix_size
#     real(kind=DP), dimension(:, :), allocatable :: matrix
#     real(kind=DP) :: row_norm
#     integer :: row, col, istat
#     real :: start_time, end_time
# 
#     call get_arguments(matrix_size)
#     allocate (matrix(matrix_size, matrix_size), stat=istat)
# 
#     ! reinitialize the matrix to avoid cache effects
#     call random_number(matrix)
#     call cpu_time(start_time)
#     do row = 1, size(matrix, 1)
#         matrix(row, :) = matrix(row, :)/sum(matrix(row, :))
#     end do
#     call cpu_time(end_time)
#     print '(A, F10.6)', 'row-wise norm: ', end_time - start_time
#     if (.not. is_normed(matrix, abs_tol=1e-4_DP)) then
#         write (unit=error_unit, fmt='(A)') 'error: array is not normalized (row-wise)'
#     end if
# 
#     ! reinitialize the matrix to avoid cache effects
#     call random_number(matrix)
#     call cpu_time(start_time)
#     do concurrent (row = 1:size(matrix, 1))
#         row_norm = 1.0_DP/sum(matrix(row, :))
#         do concurrent (col = 1:size(matrix, 2))
#             matrix(row, col) = matrix(row, col)*row_norm
#         end do
#     end do
#     call cpu_time(end_time)
#     print '(A, F10.6)', 'do concurrent row-wise norm: ', end_time - start_time
#     if (.not. is_normed(matrix, abs_tol=1e-4_DP)) then
#         write (unit=error_unit, fmt='(A)') 'error: array is not normalized (row-wise)'
#     end if
# 
#     ! initialize the matrix
#     call random_number(matrix)
#     call cpu_time(start_time)
#     matrix = matrix/spread(sum(matrix, dim=2), 2, size(matrix, 2))
#     call cpu_time(end_time)
#     print '(A, F10.6)', 'norm using spread: ', end_time - start_time
#     if (.not. is_normed(matrix, abs_tol=1e-4_DP)) then
#         write (unit=error_unit, fmt='(A)') 'error: array is not normalized (spread)'
#     end if
# 
#     deallocate (matrix)
# 
# contains
# 
#     subroutine get_arguments(matrix_size)
#         implicit none
#         integer, intent(out) :: matrix_size
#         character(len=1024) :: buffer, msg
#         integer :: istat
# 
#         if (command_argument_count() /= 1) then
#             write (unit=error_unit, fmt='(A)') 'error: expect matrix size as argument'
#             stop 1
#         end if
#         call get_command_argument(1, buffer)
#         read (buffer, fmt=*, iostat=istat, iomsg=msg) matrix_size
#         if (istat /= 0) then
#             write (unit=error_unit, fmt='(2A)') 'error: ', trim(msg)
#             stop 2
#         end if
#     end subroutine get_arguments
# 
#     function is_normed(matrix, abs_tol) result(is_okay)
#         implicit none
#         real(kind=DP), dimension(:, :), intent(in) :: matrix
#         real(kind=DP), value :: abs_tol
#         logical :: is_okay
#         
#         is_okay = all(sum(matrix, dim=2) - 1.0_DP < abs_tol)
#     end function is_normed
# 
# end program normalize_performance
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Normalize_Performance"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run -- 10 2>/dev/null")


# In[6]:


exec_status = os.system("fpm run -- 100 2>/dev/null")


# In[7]:


exec_status = os.system("fpm run -- 1000 2>/dev/null")


# In[8]:


exec_status = os.system("fpm run -- 10000 2>/dev/null")

