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
# # Print Compiler Version

# Adapted from: "Modern Fortan" by Milan Curcic (Manning)

# ```fortran
# program print_compiler_info
# 
#     use iso_fortran_env
#     implicit none
#     print *, 'Compiler version: ', compiler_version()
#     print *, 'Compiler options: ', compiler_options()
#     
# end program print_compiler_info
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Print_Compiler_Version"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

