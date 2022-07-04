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
# # Section IEEE754: Zero vs Non - Zero

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/ieee754](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/ieee754)

# ## Illustrates that 0.0 is equal to -0.0.

# ```fortran
# program zero_vs_minus_zero
#     implicit none
#     real :: zero = 0.0, minus_zero
# 
#     minus_zero = sign(zero, -1.0)
#     print '(A, 2F7.2)', '0 vs. -0: ', zero, minus_zero
#     if (zero == minus_zero) then
#         print '(A)', "Yes...."
#         print '(A)', '0 == -0'
#     else
#         print '(A)', "No...."
#         print '(A)', '0 /= -0'
#     end if
#     print '(A, F5.1)', 'sqrt(0.0) = ', sqrt(zero)
#     print '(A, F5.1)', 'sqrt(-0.0) = ', sqrt(minus_zero)
# end program zero_vs_minus_zero
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_IEEE754_Zero_vs_Non_Zero"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

