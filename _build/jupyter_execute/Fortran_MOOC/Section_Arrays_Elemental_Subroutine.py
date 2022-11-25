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
# # Section Arrays: Elemental Subroutine

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/arrays)

# ## This program demonstrates elemental subroutines in Fortran.

# ```fortran
# program elemental_subroutine
#     implicit none
#     real, dimension(3, 4) :: A, B, C
#     integer :: i
# 
#     A = reshape([ (i, i=1, 12) ], shape(A))
#     call compute(A, B, C)
#     print '(A)', 'A'
#     do i = 1, 3
#         print '(*(F7.2))', A(i, :)
#     end do
# 
#     print '(A)', 'B'
#     do i = 1, 3
#         print '(*(F7.2))', B(i, :)
#     end do
# 
#     print '(A)', 'C'
#     do i = 1, 3
#         print '(*(F7.2))', C(i, :)
#     end do
# 
# contains
# 
#     elemental subroutine compute(A, B, C)
#         implicit none
#         real, intent(in) :: A
#         real, intent(out) :: B
#         real, intent(out) :: C
# 
#         B = 2*A
#         C = 3*A
#     end subroutine compute
# 
# end program elemental_subroutine
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Arrays_Elemental_Subroutine"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# In[ ]:





# In[5]:


exec_status = os.system("fpm run 2>/dev/null")

