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
# # Section 4.1: Elsewhere Example

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate the use of the *elsewhere* construct.

# ```fortran
# program elsewhere_example
# 
#     implicit none
#     integer, parameter          :: n = 15
#     integer, dimension(n, n)    :: key
#     integer                     :: i, j
#     real, dimension(n, n)       :: a
# 
#     call random_number(a)
#     do i = 1, n
#         do j = 1, n
#             if (i > j) then
#                 ! Put negative numbers below the diagonal
#                 a(i, j) = -a(i, j) - 2.0
#             else if (i < j) then
#                 ! Put positive numbers above the diagonal
#                 a(i, j) = a(i, j) + 2.0
#             else
#                 ! Put zeros on the diagonal
#                 a(i, j) = 0.0
#             end if
#         end do
#     end do
# 
#     where (a > 0)
#         key = 1
#     elsewhere (a < 0)
#         key = -1
#     elsewhere
#         key = 0
#     end where
# 
#     write (*, "(15f5.1)") (a(i,:), i=1,n)
#     print *
#     write (*, "(15i5)") (key(i,:), i=1,n)
# end program elsewhere_example
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_4_1_Elsewhere_Example"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

