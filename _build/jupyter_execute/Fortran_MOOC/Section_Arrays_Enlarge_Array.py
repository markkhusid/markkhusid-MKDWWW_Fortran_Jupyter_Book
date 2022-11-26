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

# ## This program demonstrates enlarging an array in Fortran.

# ```fortran
# program enlarge_array
#   use, intrinsic :: iso_fortran_env, only : error_unit
#   implicit none
#   integer, parameter :: initial_size = 3, size_incr = 2
#   integer, dimension(:), allocatable :: values
#   integer :: i
#   
#   allocate (values(initial_size))
#   
#   do i = 1, size(values)
#       values(i) = i
#   end do
#   print *, values
# 
#   do i = 1, 3
#       call grow_array(values, size_incr)
#       print *, values
#   end do
# 
#   deallocate (values)
# 
#   do i = 1, 3
#       call grow_array(values, size_incr)
#       print *, values
#   end do
# 
#   deallocate (values)
# 
# contains
# 
#     subroutine grow_array(values, size_incr)
#         implicit none
#         integer, dimension(:), allocatable, intent(inout) :: values
#         integer, value ::size_incr
#         integer, dimension(:), allocatable :: new_values
#         integer :: i, size_of_values_array
# 
#         ! Added statement below to simplify allocate statement
#         size_of_values_array = size(values)
# 
#         if (allocated(values)) then
#             ! The below statement fails because values and new values are of different sizes
#             ! seems to be a Fortran version issue
#             !allocate (new_values(size_of_values_array + size_incr), source=values)
#             allocate (new_values(size_of_values_array + size_incr))
# 
#             ! For now I will just copy values into new_values using a loop
#             do i = 1, size(values)
#                 new_values(i) = values(i)
#             end do
# 
#             do i = size(values) + 1, size(new_values)
#                 new_values(i) = i
#             end do
# 
#             deallocate (values)
#             
#             call move_alloc(new_values, values)
#         else
#             allocate (values(size_incr))
#             do i = 1, size(values)
#                 values(i) = i
#             end do
#         end if
#     end subroutine grow_array
# 
# end program enlarge_array
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Enlarge_Array"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

