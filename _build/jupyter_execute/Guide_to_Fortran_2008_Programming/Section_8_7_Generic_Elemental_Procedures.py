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
# # Section 8.7: Generic Elemental Procedures

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate the generic elemental procedures.

# ``` fortran
# module swap_module
# 
#     implicit none
# 
#     public          :: swap
#     private         :: swap_reals, swap_integers
# 
#     interface swap
#         procedure swap_reals, swap_integers
#     end interface
# 
# contains
# 
#     elemental subroutine swap_reals (a, b)
#         real, intent (in out)   :: a, b
#         real                    :: temp
#         temp = a
#         a = b
#         b = temp
#     end subroutine swap_reals
# 
#     elemental subroutine swap_integers (a, b)
#         integer, intent (in out)    :: a, b
#         integer                     :: temp
#         temp = a
#         a = b
#         b = temp
#     end subroutine swap_integers
# 
# end module swap_module
# 
# program generic_elemental_procedures
# 
#     use swap_module
#     implicit none
#     integer, dimension (3)          :: &
#         i = [1, 2, 3], &
#         j = [7, 8, 9]
# 
#     real, dimension (3)             :: &
#         a = [1.1, 2.2, 3.3], &
#         b = [7.7, 8.8, 9.9]
# 
#     print *
# 
#     write (*, '(a, 3i5)') "[*] The array i is: ", i
#     write (*, '(a, 3i5)') "[*] The array j is: ", j
#     
#     print *
# 
#     write (*, '(a)') "[*] Now calling swap on the integer arrays...."
#     print *
# 
#     call swap(i, j)
# 
#     write (*, '(a, 3i5)') "[*] After swapping, the array i is: ", i
#     write (*, '(a, 3i5)') "[*] After swapping, the array j is: ", j
# 
#     print *
# 
#     write (*, '(a, 3f5.1)') "[*] The array a is: ", a
#     write (*, '(a, 3f5.1)') "[*] The array b is: ", b
# 
#     print *
# 
#     write (*, '(a)') "[*] Now calling swap on the real arrays...."
#     print *
# 
#     call swap(a, b)
# 
#     write (*, '(a, 3f5.1)') "[*] After swapping, the array a is: ", a
#     write (*, '(a, 3f5.1)') "[*] After swapping, the array b is: ", b
# 
# end program generic_elemental_procedures
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_8_7_Generic_Elemental_Procedures"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

