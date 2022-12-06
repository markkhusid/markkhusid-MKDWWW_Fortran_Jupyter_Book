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
# # Section Arrays: Normalize
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program normalizes a randomly generated matrix in Fortran.

# ```fortran
# program normalize
#   use, intrinsic :: iso_fortran_env, only : error_unit, DP => REAL64
#   implicit none
#   integer, parameter :: rows = 3, cols = 4
#   real(kind=DP), dimension(rows, cols) :: matrix, spread_norm
#   real(kind=DP), dimension(rows) :: norm
# 
#   call random_number(matrix)
#   print '(A)', 'original:'
#   call print_matrix(matrix)
# 
#   norm = sum(matrix, dim=2)
#   print '(A, *(F12.7))', 'norm:', norm
# 
#   spread_norm = spread(norm, 2, size(matrix, 2))
#   call print_matrix(spread_norm)
# 
#   matrix = matrix/spread_norm
#   print '(A)', 'row-normalized::'
#   call print_matrix(matrix)
# 
#   norm = sum(matrix, dim=2)
#   print '(A, *(F12.7))', 'norm:', norm
# 
# contains
# 
#   subroutine print_matrix(matrix)
#       implicit none
#       real(kind=DP), dimension(:, :), intent(in) :: matrix
#       integer :: row
# 
#       do row = 1, size(matrix, 1)
#           print '(*(F12.7))', matrix(row, :)
#       end do
#   end subroutine print_matrix
# 
# end program normalize
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Normalize"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")


# In[6]:


exec_status = os.system("fpm run 2>/dev/null")


# In[7]:


exec_status = os.system("fpm run 2>/dev/null")

