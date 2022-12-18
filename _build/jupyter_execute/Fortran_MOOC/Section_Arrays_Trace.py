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
# # Section Arrays: Trace
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Trace"
code_app_dir = code_dir + "/" + "app"


# In[3]:


os.chdir(code_app_dir)


# ## This program demonstrates computing the trace of a matrix  in Fortran.

# In[4]:


get_ipython().run_cell_magic('capture', '', "%%writefile section_arrays_trace.f90\nprogram compute_trace\n    implicit none\n    integer :: i\n    real, dimension(5, 5) :: A\n\n    call random_number(A)\n    do i = 1, size(A, 1)\n        print '(5F7.4)', A(i, :)\n    end do\n    print '(/, A, F7.4)', 'trace = ', trace(A)\n\ncontains\n\n    real function trace(matrix)\n        use, intrinsic :: iso_fortran_env, only : error_unit\n        implicit none\n        real, dimension(:, :), intent(in) :: matrix\n        integer :: i\n\n        if (size(matrix, 1) /= size(matrix, 2)) then\n            write (unit=error_unit, fmt='(A)') &\n                'error: can not compute trace of a non-square matrix'\n            stop 1\n        end if\n        trace = 0.0\n        do i = 1, size(matrix, 1)\n            trace = trace + matrix(i, i)\n        end do\n    end function trace\n\nend program compute_trace")


# In[5]:


get_ipython().system('bat section_arrays_trace.f90')


# The above program is compiled and run using Fortran Package Manager (fpm):

# In[6]:


os.chdir(code_dir)


# ## Build the Program using FPM (Fortran Package Manager)

# In[7]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[8]:


exec_status = os.system("fpm run 2>/dev/null")

