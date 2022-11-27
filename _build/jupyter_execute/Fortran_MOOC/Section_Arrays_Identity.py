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
# # Section Arrays: Enlarge Array

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates reading in command line arguments in Fortran.

# ```fortran
# program identity
#     use, intrinsic :: iso_fortran_env, only : error_unit
#     implicit none
#     integer :: n, i, istat
#     real, dimension(:, :), allocatable :: A
# 
#     n = get_size()
#     allocate(A(n, n), stat=istat)
#     if (istat /= 0) then
#         write (unit=error_unit, fmt='(A)') &
#             'error: can not allocate array'
#         stop 3
#     end if
#     A = eye(n)
#     do i = 1, size(A, 1)
#         print *, A(i, :)
#     end do
#     deallocate(A)
# 
# contains
# 
#     function get_size() result(n)
#         use, intrinsic :: iso_fortran_env, only : error_unit
#         implicit none
#         integer :: n
#         integer :: istat
#         character(len=1024) :: buffer, msg
# 
#         if (command_argument_count() /= 1) then
#             write (unit=error_unit, fmt='(A)') &
#                 'error: expecting an integer argument, size of array'
#             stop 1
#         end if
#         call get_command_argument(1, buffer)
#         read (buffer, fmt=*, iostat=istat, iomsg=msg) n
#         if (istat /= 0) then
#             write (unit=error_unit, fmt='(2A)') &
#                 'error: ', msg
#             stop 2
#         end if
#     end function get_size
# 
#     function eye(n) result(matrix)
#         implicit none
#         integer, value :: n
#         real, dimension(n, n) :: matrix
#         integer :: i
# 
#         matrix = 0.0
#         do i = 1, size(A, 1)
#             matrix(i, i) = 1.0
#         end do
#     end function eye
# 
# end program identity
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Identity"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run -- 3 2>/dev/null")


# In[6]:


exec_status = os.system("fpm run -- 5 2>/dev/null")

