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
# # Section Arrays: Submatrices
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates matrix slicing in Fortran.

# ```fortran
# program submatrices
#   implicit none
#   integer, dimension(3, 4) :: A
#   integer, dimension(12)   :: A_array
#   integer :: i, j
# 
#   A_array = [ (((i - 1)*size(A, 2) + j, &
#                    j=1, size(A, 2)), &
#                    i=1, size(A, 1)) ]
# 
#   A = reshape([ (((i - 1)*size(A, 2) + j, &
#                    j=1, size(A, 2)), &
#                    i=1, size(A, 1)) ], &
#               shape(A))
#               
#   
#   print *, "A_array contains: ", A_array
# 
#   print *, "A matrix contains: "
#   
#   do i = 1, size(A, 1)
#     print *, A(i, :)
#   end do
# 
#   print *
#   print *, "Row 2 contains: "
#   print *, A(2, :)
#   print *, "Column 3 contains: "
#   print *, A(:, 3)
#   print '(A, I0)', 'rank = ', rank(A(2, :))
#   print '(A, I0)', 'shape = ', shape(A(2, :))
# end program submatrices
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Submatrices"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

