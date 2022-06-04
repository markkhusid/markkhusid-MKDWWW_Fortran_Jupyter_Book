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
# # Section 8.8: Findloc Function

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate the *findloc* function.

# ```fortran
# program find_loc
# 
#     implicit none
# 
#     intrinsic :: findloc
# 
#     real, dimension (3,3)   :: X =          &
#         reshape (                           &
#                     [   -11,  12, -13,      &
#                          21,  22, -23,      &
#                          31, -32, -33 ],    &
#                     [ 3, 3 ], order = [ 2, 1 ] )
# 
#     logical, parameter      :: T = .true.
# 
#     write (*,'(a)') "[*] The matrix X"
#     call write_matrix(X)
# 
#     write (*,*)
# 
#     write (*,'(a)') "[*] Begin findloc call..."
#     write (*,'(a)') "findloc( X > 0, T )"
#     write (*,'(a, 2i2, a)')  "The first element where (i,j) > 0 is: (", &
#         findloc( X > 0, T ), &
#         ") in column major order."            ! = [ 2, 1 ]
# 
#     contains
# 
#         subroutine write_matrix(a)
#             real, dimension(:,:), intent(in) :: a
#             integer :: i, j
#             do i = lbound(a,1), ubound(a,1)
#                 write (*,*) (a(i,j), j = lbound(a,2), ubound(a,2))
#             end do
#         end subroutine write_matrix
# 
# end program find_loc
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_8_8_Findloc_Function"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

