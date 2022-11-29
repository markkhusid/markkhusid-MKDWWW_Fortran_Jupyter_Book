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
# # Section Arrays: Matrix
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates a 2D matrix in Fortran.

# ```fortran
# program matrix
#   implicit none
#   integer, parameter :: ROWS = 3, COLS = 5
#   real, dimension(ROWS, COLS) :: A
#   integer :: i, j
#   real :: total
# 
#   A = reshape([ (((i - 1)*size(A, 2) + j, j=1,size(A, 2)), i=1,size(A, 1)) ], &
#               shape(A))
#   do i = 1, size(A, 1)
#       print *, A(i, :)
#   end do
#   total = 0.0
#   do j = 1, size(A, 2)
#       do i = 1, size(A, 1)
#           total = total + A(i, j)**2
#       end do
#   end do
#   print '(/, A, F10.2)', 'total = ', total
# end program matrix
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Matrix"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

