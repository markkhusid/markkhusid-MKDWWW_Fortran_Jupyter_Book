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
# # Section 3.8: Argument Passing

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate different methods of passing arguments to functions in Fortran.

# This program calculates the sum:

# $$
# \Large \sum_{i=m}^n \left(s+d \times i \right)
# $$

# ``` fortran
# program series_sum_program
# 
#     implicit none
#     
#     integer, parameter :: n = 100
#     
#     ! Shows different ways to pass arguments to a function
#     print *, series_sum(0, 700, 100.0, 0.1)
#     print *, series_sum(0, 700, d=0.1, s=100.0)
#     print *, series_sum(n=700, d=0.1, s=100.0)
#     print *, series_sum(d=0.1, s=100.0, n=700)
#     print *, series_sum(m=0, n=700, d=0.1, s=100.0)
# 
# contains
# 
#     function series_sum(m, n, s, d) result (series_sum_result)
#         integer, optional, intent(in)   :: m
#         integer, intent(in)             :: n
#         real, intent(in)                :: s, d
#         real                            :: series_sum_result
#         integer                         :: i, temp_m
# 
#         if (present(m)) then
#             temp_m = m
#         else
#             temp_m = 0
#         end if
# 
#         series_sum_result = 0
#         do i = temp_m, n
#             series_sum_result = series_sum_result + s + i * d
#         end do
# 
# end function series_sum
# 
# end program series_sum_program
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_3_8_Argument_Passing"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

