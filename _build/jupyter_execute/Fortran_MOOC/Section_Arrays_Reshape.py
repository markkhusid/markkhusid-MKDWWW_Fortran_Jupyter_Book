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
# # Section Arrays: Reshape
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program reshapes an array into a matrix in Fortran.

# ```fortran
# program reshape_test
#     implicit none
#     integer, parameter :: nr_values = 12
#     integer :: i
#     integer, dimension(nr_values) :: values = [ (i, i=1, nr_values) ]
#     integer, dimension(2, 5) :: too_small
#     integer, dimension(3, 5) :: too_large
# 
#     too_small = reshape(values, shape(too_small))
#     call print_matrix(too_small)
# 
#     too_large = reshape(values, shape(too_large), pad=[-1, -2])
#     call print_matrix(too_large)
# 
# contains
# 
#     subroutine print_matrix(A)
#         implicit none
#         integer, dimension(:, :), intent(in) :: A
#         integer :: i
# 
#         do i = 1, size(A, 1)
#             print *, A(i, :)
#         end do
#     end subroutine print_matrix
# 
# end program reshape_test
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Reshape"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

