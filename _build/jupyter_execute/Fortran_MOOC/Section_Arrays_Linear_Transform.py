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
# # Section Arrays: Linear Transform
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates an elemental function with multiple arguments in Fortran.

# ```fortran
# program linear_transform
#   implicit none
#   real, dimension(5) :: values
#   real, dimension(2) :: a = [ 1.1, 2.2 ], &
#                         x = [ 0.5, 2.0 ], &
#                         b = [ -1.2, 2.5 ]
#   integer :: i
# 
#   call random_number(values)
#   print *, "The contents of the valus array is:"
#   print *, values
#   print *, "lin_transform(values, 2.0, 1.0) = "
#   print *, lin_transform(values, 2.0, 1.0)
#   print *, "lin_transform(x, a, b) = "
#   print *, lin_transform(x, a, b)
# 
# contains
# 
#   elemental real function lin_transform(x, a, b)
#       implicit none
#       real, intent(in) :: x, a, b
# 
#       lin_transform = a*x + b
#   end function lin_transform
# 
# end program linear_transform
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Linear_Transform"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")


# In[6]:


exec_status = os.system("fpm run 2>/dev/null")

