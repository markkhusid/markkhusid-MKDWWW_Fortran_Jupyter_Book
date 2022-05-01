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
# # Cold Front Calculator

# Adapted from: "Modern Fortan" by Milan Curcic (Manning)

# ## Program to Calculate the Temperature due to a Cold Front

# ```fortran
# program cold_front
# 
#     implicit none
#     
#     real :: temp1 = 12 ! degrees C
#     real :: temp2 = 24 ! degrees C
#     real :: dx = 960   ! km
#     real :: c = 20     ! km / hr
#     real :: dt = 24    ! hours
#     
#     real :: res        ! result in degrees C
#     
#     res = temp2 - c * (temp2 - temp1) / dx * dt
#     
#     print *, "Temperature after ", dt, &
#              "hours is ", res, "degrees"
#              
# end program cold_front
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Cold_Front_Calculator"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

