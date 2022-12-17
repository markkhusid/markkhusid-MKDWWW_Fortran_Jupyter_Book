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
# # Section Arrays: Subarrays
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates array slicing in Fortran.

# ```fortran
# program subarrays
#   implicit none
#   integer :: i
#   integer, dimension(10) :: A = [ (i, i = 1, 10) ]
#   character(len=10), parameter :: FMT = '(10I3)'
# 
#   print FMT, A
#   print FMT, A(4:7)
#   print FMT, A(:7)
#   print FMT, A(4:)
#   print FMT, A(4:7:2)
#   print FMT, A(4::2)
#   print FMT, A(:7:2)
#   print FMT, A(7:4:-1)
# end program subarrays
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Subarrays"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

