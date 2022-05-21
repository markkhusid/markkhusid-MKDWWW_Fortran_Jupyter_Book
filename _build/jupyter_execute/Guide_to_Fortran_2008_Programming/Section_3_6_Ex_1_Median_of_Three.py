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
# # Section 3.6: Median of Three

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program that finds the median of three numbers.

# ``` fortran
# program median_of_3_program
# 
#     implicit none
# 
#     real :: num1, num2, num3
#     real :: median
#     
#     write (*, '(a)') "This program finds the median of three numbers....."
#     write (*, '(a)') "Data piped in from command line...."
#     read *, num1, num2, num3
#     
#     write (*, '(a, 3f10.2)') "The three entered numbers were -->", num1, num2, num3
#     
#     median = medianOf3(n1=num1, n2=num2, n3=num3)
#     
#     write (*, '(a, f10.2)') "The median value is -->", median
#  
#     contains
# 
#         subroutine swap(a, b)
#             real, intent (in out) :: a, b
#             real :: temp
#             temp = a
#             a = b
#             b = temp
#         end subroutine swap
#     
#         subroutine sort(val1, val2, val3)
#             real, intent(in out) :: val1, val2, val3
#         
#             if (val1 > val2) then
#                 call swap (val1, val2)
#             end if
#             if (val1 > val3) then
#                 call swap (val1, val3)
#             end if
#             if (val2 > val3) then
#                 call swap (val2, val3)
#             end if
#         end subroutine sort
# 
#         function medianOf3(n1, n2, n3) result (median_value)
#  
#             real, intent(in out) :: n1, n2, n3
#             real :: median_value
#         
#             call sort (val1=n1, val2=n2, val3=n3)
#             
#             median_value = n2
#      
#         end function medianOf3
# 
# end program median_of_3_program
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_3_6_Ex_1_Median_of_Three"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("echo '87 12 55' | fpm run | sed 1,1d")

