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
# # Section 9.3: Difference Between Sum of Squares and Square of Sums

# Adapted from: "Introduction to Programming using Fortran 95/2003/2008" by Ed Jorgensen (March 2018 / Version 3.0.51)

# ## Program to Calculate the Difference Between the Sum of Squares and the Square of Sums

# ```fortran
# program SOSdifference
# 
#     ! declare variables
#     implicit none
#     integer :: i, n, SumOfSqrs = 0, SqrOfSums = 0, difference
# 
#     ! display initial header
# 
#     !write (*,*) "Example Program"
#     print *
#     write (*,'(a)') "This program calculates the"
#     write (*,'(a)') "difference between sum of squares "
#     write (*,'(a)') "and square of sums"
# 
#     ! prompt for and read the n value
#     !write (*,*) "Enter N value: "
#     !read  (*,*) n
#     ! Set n = 100 for Jupyter Notebook
#     n = 100
# 
#     ! loop from 1 to n
# 
#     do i = 1, n
#         ! compute sum of squares
#         SumOfSqrs = SumOfSqrs + i ** 2
# 
#         ! compute square of sums
#         SqrOfSums = SqrOfSums + i
#     end do
# 
#     ! square the sums
#     SqrOfSums = SqrOfSums ** 2
# 
#     ! compute the difference between sum of squares and square of sums  
#     difference = SqrOfSums - SumOfSqrs
# 
#     ! display results
#     print *
#     write (*,'(a)') "Results..."
#     print *
#     write (*, '(a, i5, a, i10)') "The square of the sums from 1 to ", n, " is -> ", SqrOfSums
#     print *
#     write (*, '(a, i5, a, i10)') "The sum of the squares from 1 to ", n, " is -> ", SumOfSqrs
#     print *
#     write (*,'(a, i10)') "The difference between the square of the sums and sum of the squares is -> ", difference
#     print *
# end program SOSdifference
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_9_3_SOS_Difference"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

