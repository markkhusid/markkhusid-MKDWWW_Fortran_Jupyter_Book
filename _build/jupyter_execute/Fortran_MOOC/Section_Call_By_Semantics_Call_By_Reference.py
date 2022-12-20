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
# # Section Call By Semantics: Call By Reference
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/call_by_semantics](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/call_by_semantics)

# ## This program demonstrates calling by reference in Fortran.

# ```fortran
# program call_by_reference
#     implicit none
#     integer :: m
#     m = 5
#     print *, m
#     call increment(m)
#     print *, m
# 
# contains
# 
#     subroutine increment(n)
#         implicit none
#         integer, intent(inout) :: n
# 
#         n = n + 1
#     end subroutine increment
# 
# end program call_by_reference
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Call_By_Semantics_Call_By_Reference"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%writefile section_call_by_semantics_call_by_reference.f90\nprogram call_by_reference\n    implicit none\n    integer :: m\n    m = 5\n    print *, m\n    call increment(m)\n    print *, m\n\ncontains\n\n    subroutine increment(n)\n        implicit none\n        integer, intent(inout) :: n\n\n        n = n + 1\n    end subroutine increment\n\nend program call_by_reference')


# In[6]:


get_ipython().system('bat *.f90')


# In[7]:


os.chdir(code_dir)


# In[8]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[9]:


exec_status = os.system("fpm run 2>/dev/null")

