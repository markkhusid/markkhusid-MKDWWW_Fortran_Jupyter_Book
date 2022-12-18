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
# # Section Call By Semantics: Call By In Reference
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates calling by in reference in Fortran.

# ```fortran
# program call_by_in_reference
#     implicit none
# 
#     print *, "5! = ", factorial(5)
#     print *, "10! = ", factorial(10)
#     print *, "12! = ", factorial(12)
# 
# contains
# 
#     function factorial(arg) result(fac)
#         implicit none
#         integer, intent(in) :: arg
#         integer :: fac, n
# 
#         n = arg
#         fac = 1
#         do while (n > 1)
#             fac = fac*n
#             n = n - 1
#         end do
#     end function factorial
# 
# end program call_by_in_reference
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Call_By_Semantics_Call_By_In_Reference"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%writefile section_call_by_semantics_call_by_in_reference.f90\nprogram call_by_in_reference\n    implicit none\n\n    print *, "5! = ", factorial(5)\n    print *, "10! = ", factorial(10)\n    print *, "12! = ", factorial(12)\n\ncontains\n\n    function factorial(arg) result(fac)\n        implicit none\n        integer, intent(in) :: arg\n        integer :: fac, n\n\n        n = arg\n        fac = 1\n        do while (n > 1)\n            fac = fac*n\n            n = n - 1\n        end do\n    end function factorial\n\nend program call_by_in_reference')


# In[6]:


os.chdir(code_dir)


# In[7]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[8]:


exec_status = os.system("fpm run 2>/dev/null")

