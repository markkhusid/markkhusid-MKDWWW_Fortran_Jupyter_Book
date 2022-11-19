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
# # Section Arrays: Allocate from Source

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates allocating an array from a source array.

# ```fortran
# program allocate_from_source
#     use, intrinsic :: iso_fortran_env, only : error_unit
#     implicit none
#     integer, dimension(3, 2) :: A
#     integer, dimension(:, :), allocatable :: B
#     integer :: i, status
# 
#     A = reshape([ (i, i=1, size(A)) ], shape(A))
#     allocate(B, source=A, stat=status)
#     if (status /= 0) then
#         write (unit=error_unit, fmt='(A)') 'error: can not allocate array'
#         stop 1
#     end if
#     print *, 'The matrix A contains:'
#     do i = 1, size(A, 1)
#         print '(*(I4))', A(i, :)
#     end do
#     print *
#     print *, 'The matrix B contains:'
#     do i = 1, size(A, 1)
#         print '(*(I4))', A(i, :)
#     end do
#     deallocate (B)
# end program allocate_from_source
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Allocate_from_Source"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

