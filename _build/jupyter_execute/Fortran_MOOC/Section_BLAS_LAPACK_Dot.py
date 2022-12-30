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
# # Section: BLAS/LAPACK - Dot Product
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack)

# ## This program demonstrates performing a dot product in Fortran.

# ### Dot Products

# In this notebook we will use Fortran to perform dot products on vectors and matrices.

# The dot product of two vectors in 3-space is given by:

# $$
# \Large \mathbf{u} \cdot \mathbf{v} =
# u_1 v_1 + u_2 v_2 + u_3 v_3
# $$

# where:

# $$
# \Large \mathbf{u} =
# \left[
# \begin{array}{c}
# u_{1}  \\
# u_{2}  \\
# u_{3}
# \end{array}
# \right]
# $$

# and

# $$
# \Large \mathbf{v} =
# \left[
# \begin{array}{c}
# v_{1}  \\
# v_{2}  \\
# v_{3}
# \end{array}
# \right]
# $$

# The approach makes use of the BLAS/LAPACK linear equation solver routine called **SDOT**.  Information on this routine can be found at [LAPACK - SDOT](https://netlib.org/lapack/explore-html/df/d28/group__single__blas__level1_ga37a14d8598319955b711af0d64a6f56e.html#ga37a14d8598319955b711af0d64a6f56e).
# 
# The driver program is called *dot_test* and is listed below:

# ### In file dot_test.f90

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Dot/app/section_blas_lapack_dot.f90
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

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Dot/fpm.toml
# ---
# language: toml
# ---
# ```

# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_BLAS_LAPACK_Dot"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status =     os.system("fpm run 2>/dev/null")

