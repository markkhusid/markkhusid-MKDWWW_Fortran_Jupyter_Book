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
# # Cold Front Calculator With Loop

# Adapted from: "Modern Fortan" by Milan Curcic (Manning)

# ```fortran
# program cold_front
# 
#     implicit none
#     integer :: n
#     real    :: nhours
#     
#     do n = 6, 48, 6
#         nhours = real(n)
#         print *, "Temperature after ", &
#             nhours, " hours is ", &
#             cold_front_temperature(12., 24., 20., 960., nhours), " degrees."
#     end do
#     
# contains
# 
#     real function cold_front_temperature ( &
#         temp1, temp2, c, dx, dt) result(res)
#         
#         real, intent(in) :: temp1, temp2, c, dx, dt
#         res = temp2 - c * (temp2 - temp1) / dx * dt
#         
#     end function cold_front_temperature
#     
# end program cold_front
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Cold_Front_Calculator_with_Loop"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")


# In[ ]:




