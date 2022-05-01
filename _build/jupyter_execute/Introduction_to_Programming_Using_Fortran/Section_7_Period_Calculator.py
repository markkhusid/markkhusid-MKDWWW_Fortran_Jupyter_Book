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
# # Section 7: Pendulum Period Calculator

# Adapted from: "Introduction to Programming using Fortran 95/2003/2008" by Ed Jorgensen (March 2018 / Version 3.0.51)

# ## Program to Calculate the Period of a Pendulum

# ```fortran
# program period
# 
#     ! Program to calculate the period of a pendulum
# 
#     ! Declare variables
#     !   real constants -> gravity, pi
#     !   reals -> angle, length, alpha
# 
#     implicit none
# 
#     real                :: angle, length, pperiod, alpha
#     real, parameter     :: gravity = 980.0, pi = 3.14159
# 
#     ! display initial header
#         
#         write (*,'(a)') "Pendulum Period Calculation Program"
#         print *
# 
#     ! prompt for and read the length of the angle values
#     ! for the website, we will hard code the length and angle
# 
#         !write (*,'(a)', advance="no") "Enter the Length and Angle values: "
#         !read (*,*) length, angle
#         length = 1 ! meters
#         angle = 10 ! degrees
# 	    write (*, '(a, f8.2, a)') "The Length is: ", length, " meters"
# 	    write (*, '(a, f8.2, a)') "The Angle  is: ", angle , " degrees"
# 
#     ! convert degrees to radians
#         alpha = angle * pi / 180.0
# 
#     ! calculate the period
#         pperiod = 2.0 * pi * sqrt(length / gravity) * ( 1.0 + 1.0/4.0 * sin( alpha / 2.0 )**2)
# 
#     ! display the results
#         print *
#         write (*, '(a)') "Calculating Results......"
#         write (*,'(a, f8.2, a)') "The period is: ", pperiod, " seconds."
#         print *
# 
# end program period
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_7_Period_Calculator"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

