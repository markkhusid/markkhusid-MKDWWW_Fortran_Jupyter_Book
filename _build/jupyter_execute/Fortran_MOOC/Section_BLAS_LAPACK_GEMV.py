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
# # Section: BLAS/LAPACK - GEMV
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack)

# ## This program demonstrates using the GEMV BLAS/LAPACK subroutine to perform a matrix vector product in Fortran.

# In file *section_blas_lapack_gemv.f90*

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_GEMV/app/section_blas_lapack_gemv.f90
# ---
# language: fortran
# ---
# ```

# In file *util_mod.f90*

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_GEMV/src/util_mod.f90
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

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_GEMV/fpm.toml
# ---
# language: toml
# ---
# ```

# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_BLAS_LAPACK_GEMV"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status =     os.system("fpm run 2>/dev/null")

