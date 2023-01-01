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
# # Section: BLAS/LAPACK - DDOT Timing
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack)

# ## This program demonstrates copying vectors using BLAS/LAPACK in Fortran.

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_DDOT_Timing/app/section_blas_lapack_ddot_timing.f90
# ---
# language: fortran
# ---
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# Since the code makes use of the LAPACK library, the following FPM configuration file (fpm.toml) was used:

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_DDOT_Timing/fpm.toml
# ---
# language: toml
# ---
# ```

# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_BLAS_LAPACK_DDOT_Timing"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 1000")


# In[6]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 10000")


# In[7]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 100000")


# In[8]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 1000000")


# In[9]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 10000000")


# In[10]:


exec_status =     os.system("fpm run 2>/dev/null -- 1 100000000")


# In[11]:


exec_status =     os.system("fpm run 2>/dev/null")

