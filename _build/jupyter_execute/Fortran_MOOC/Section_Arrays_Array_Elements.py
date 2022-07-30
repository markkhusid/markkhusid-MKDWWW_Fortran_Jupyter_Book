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
# # Section Arrays: Array Elements

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates array element indexing.

# ```fortran
# program array_elements
#     implicit none
#     integer, dimension(5) :: A
#     integer :: i
# 
#     A(1) = 1
#     do i = 2, size(A)
#         A(i)  = 2*A(i - 1)
#     end do
#     print *, A
# end program array_elements
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Array_Elements"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# fpm run output now sends messages to stderr.  We redirect these messages to /dev/null for suppression.

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

