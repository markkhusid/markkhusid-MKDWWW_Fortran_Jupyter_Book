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
# # Section Arrays: Assumed

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates a Fortran technique.

# ```fortran
# program assumed
#     implicit none
#     integer :: i
#     integer, dimension(5) :: array1d = [ 2, 3, 5, 7, 11 ]
# 
#     print *, array1d
#     call factorial(array1d)
#     print *, array1d
# contains
# 
#     integer function fac(n)
#         implicit none
#         integer, value :: n
#         integer :: i
# 
#         fac = 1
#         do i = 2, n
#             fac = fac*i
#         end do
#     end function fac
# 
#     subroutine factorial(A)
#         implicit none
#         integer, dimension(:), intent(inout) :: A
#         integer :: i
# 
#         do i = 1, size(A)
#             A(i) = fac(A(i))
#         end do
#     end subroutine factorial
# 
# end program assumed
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Assumed"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

