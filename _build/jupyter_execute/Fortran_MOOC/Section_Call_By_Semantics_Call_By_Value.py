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
# # Section Call By Semantics: Call By Value
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/call_by_semantics](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/call_by_semantics)

# ## This program demonstrates calling by value in Fortran.

# ```fortran
# program call_by_value
#     implicit none
#     integer :: n
# 
#     n = 5
#     print *, n, "! = ", factorial(n)
#     
#     print *
#     
#     n = 6
#     print *, n, "! = ", factorial(n)
# 
# contains
# 
#     function factorial(n) result(fac)
#         implicit none
#         integer, value :: n
#         integer :: fac
# 
#         fac = 1
#         do while (n > 1)
#             fac = fac*n
#             n = n - 1
#         end do
#     end function factorial
# 
# end program call_by_value
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Call_By_Semantics_Call_By_Value"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%writefile section_call_by_semantics_call_by_value.f90\nprogram call_by_value\n    implicit none\n    integer :: n\n\n    n = 5\n    print *, n, "! = ", factorial(n)\n    \n    print *\n    \n    n = 6\n    print *, n, "! = ", factorial(n)\n\ncontains\n\n    function factorial(n) result(fac)\n        implicit none\n        integer, value :: n\n        integer :: fac\n\n        fac = 1\n        do while (n > 1)\n            fac = fac*n\n            n = n - 1\n        end do\n    end function factorial\n\nend program call_by_value')


# In[6]:


get_ipython().system('bat *.f90')


# In[7]:


os.chdir(code_dir)


# In[8]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[9]:


exec_status = os.system("fpm run 2>/dev/null")

