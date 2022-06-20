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
# # Section 8.1: Submodules

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate use of submodules.

# ```fortran
# module line_mod
# 
#       implicit none
#       private
# 
#       type, public :: line
#           real :: x1, y1, x2, y2
# 
#           contains
#               procedure :: length
#       end type line
# 
#       interface
#           module function length (l)
#               class(line), intent(in)  :: l
#               real :: length
#           end function length
#       end interface
# 
# end module line_mod
# 
# submodule (line_mod) line_length_mod
# 
#       contains
#           module procedure length
# 
#               length = sqrt((l%x2 - l%x1)**2 + (l%y2 - l%y1)**2)
#           end procedure length
# 
# end submodule line_length_mod
# 
# program submod
# 
#           use line_mod
#           implicit none
#           type (line)   :: line_1
#           line_1 = line(0, 0, 1, 1)
#           write (*, '(a)') "**** Line Length Calculation Program ****"
# 
#           print *
#           write (*, '(a)') "Coordinates....."
#           write (*, '(a, f15.1)') "Y2: ", line_1%y2
#           write (*, '(a, f15.1)') "Y1: ", line_1%y1
#           write (*, '(a, f15.1)') "X2: ", line_1%x2
#           write (*, '(a, f15.1)') "X1: ", line_1%x1
# 
#           print *
#           write (*, '(a, f10.4)') "The line length is -> ", line_1%length()
# 
# end program submod
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_8_1_Submodules"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

