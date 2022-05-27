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
# # Section 1.16: Factorial Recursion

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to calculate factorials using recursion in Fortran.

# ```fortran
# module factorial_module
# 
#     implicit none
#     public :: factorial
# 
# contains
# 
#     recursive function factorial(n) result (factorial_result)
# 
#         integer, intent(in) :: n
#         integer :: factorial_result
# 
#         if (n <= 0) then
#             factorial_result = 1
#         else
#             factorial_result = n * factorial(n - 1)
#         end if
# 
#     end function factorial
# 
# end module factorial_module
# 
# program test_factorial
#     
#     use factorial_module
#     implicit none
# 
#     integer :: n
# 
#     read *, n ! Will be piped in from command line
#     print *
#     write (unit = *, fmt = "(i10, a, i10)") n, "! = ", factorial(n)
# 
# end program test_factorial
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_1_16_Factorial_Recursion"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# ## Calculate:

# $$
# \Large 3!
# $$

# In[5]:


exec_status = os.system("echo 3 | fpm run | sed 1,1d")


# ## Calculate:

# $$
# \Large 6!
# $$

# In[6]:


exec_status = os.system("echo 6 | fpm run | sed 1,1d")


# ## Calculate:

# $$
# \Large 15!
# $$

# In[7]:


exec_status = os.system("echo 15 | fpm run | sed 1,1d")

