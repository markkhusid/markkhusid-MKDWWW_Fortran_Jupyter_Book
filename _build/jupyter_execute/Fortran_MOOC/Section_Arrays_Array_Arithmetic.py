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
# # Section Arrays: Array Arithmetic

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates array arithmetic.

# ```fortran
# program array_arithmetic
#     implicit none
#     real, dimension(5) :: A = [ 1.2, 2.3, 3.4, 4.5, 5.6 ], &
#                           B = [ -1.0, -0.5, 0.0, 0.5, 1.0], &
#                           C
# 
#     print *, "The array A contains: "
#     print *, A
# 
#     print *
# 
#     print *, "The array B contains: "
#     print *, B
# 
#     print *
# 
#     C = A + 2.0*B
# 
#     print *, "C = A + 2.0 * B"
#     print *, "The array C containes"
# 
#     print *, C
# end program array_arithmetic
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Array_Arithmetic"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# fpm run output now sends messages to stderr.  We redirect these messages to /dev/null for suppression.

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

