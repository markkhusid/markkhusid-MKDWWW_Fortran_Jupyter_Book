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
# # Section Arrays: Max Array
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates the **maxval** and **maxloc** intrinsic functions in Fortran.

# ```fortran
# program max_array
#     implicit none
#     integer, dimension(3, 4) :: A
#     integer :: i, j
#     character(len=10), parameter :: FMT = '(A, 4I13)'
# 
#     A = reshape (  [ &
#                     ( &
#                       ((i - 1)*size(A, 2) + j, &
#                         j=1,size(A, 2)), &
#                         i=1,size(A, 1) &
#                     ) &
#                   ], &
#                   shape(A) &
#                 ) - 8
# 
#     ! Print out array
#     do i = 1, size(A, 1)
#         print *, A(i, :)
#     end do
# 
#     print *
# 
#     print FMT, 'maximum =                       ', maxval(A)
#     print FMT, 'row maximum =                   ', maxval(A, dim=1)
#     print FMT, 'column maximum =                ', maxval(A, dim=2)
#     print FMT, 'maximum odd elment =            ', maxval(A, mask=mod(A, 2) /= 0)
#     print FMT, 'row maximum negative element =  ', maxval(A, dim=2, mask=A < 0)
#     print FMT, 'maxloc (row, col) =             ', maxloc(A)
#     print FMT, 'column maxloc (columns) =       ', maxloc(A, dim=2)
# end program max_array
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Max_Array"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

