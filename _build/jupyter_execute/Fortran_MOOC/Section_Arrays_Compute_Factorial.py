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
# # Section Arrays: Compute Factorial

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates computing the factorials over an array of integers in Fortran.

# ```fortran
# program compute_factorial
#     implicit none
#     integer :: i
#     integer, dimension(5) :: values = [ (i, i=1,5) ]
# 
#     print *, values
#     print *, factorial(values)
# 
# contains
# 
#     elemental integer function factorial(n)
#         implicit none
#         integer, value :: n
#         integer :: i
# 
#         factorial = 1
#         do i = 2, n
#             factorial = factorial*i
#         end do
#     end function factorial
# 
# end program compute_factorial
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Compute_Factorial"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

