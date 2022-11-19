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
# # Section Arrays: Array Initialization

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates initializing arrays in Fortran.

# ```fortran
# program array_initialization
#   implicit none
#   integer :: i
#   integer, dimension(5) :: A, B, C
# 
#   A = 13
#   B = [ 2, 3, 5, 7, 11 ] 
#   C = [ (2**i, i=0,4) ] 
#   print *, A
#   print *, B
#   print *, C
# end program array_initialization
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Array_Initialization"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

