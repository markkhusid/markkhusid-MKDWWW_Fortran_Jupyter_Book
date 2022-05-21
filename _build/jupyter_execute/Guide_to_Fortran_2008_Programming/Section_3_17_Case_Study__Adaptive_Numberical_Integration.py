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
# # Section 3.17: Case Study: Adaptive Numerical Integration

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to demonstrate the modules and procedures in Fortran.

# This program calculates the integral:

# $$
# \Large \int_{-4}^4 e^{x^2} d{x}
# $$

# using adaptive numberical integration.

# ```fortran
# module math_module
#     implicit none
#     private
#     real, public, parameter :: pi    = 3.1415926
#     real, public, parameter :: e     = 2.7182818
#     real, public, parameter :: gamma = 0.5772156
# end module math_module
# 
# module function_module
# 
#     implicit none
#     private
#     public :: f
# 
# contains
#     function f(x) result (f_result)
#         real, intent(in)        :: x
#         real                    :: f_result
# 
#         f_result = exp(-x**2.0)
#     end function f
# end module function_module
# 
# 
# module integral_module
# 
#     implicit none
#     private
#     public :: integral
# 
# contains
# 
#     recursive function integral(f, a, b, tolerance) result (integral_result)
# 
#         intrinsic :: abs
# 
#         interface
#             function f(x) result (f_result)
#                 real, intent(in) :: x
#                 real :: f_result
#             end function f
#         end interface
# 
#         real, intent(in)    :: a, b, tolerance
#         real                :: integral_result
#         real                :: h, mid
#         real                :: one_trapezoid_area, two_trapezoid_area
#         real                :: left_area, right_area
# 
#         h = b - a
#         mid = (a + b) / 2
#         one_trapezoid_area = h * (f(a) + f(b)) / 2.0
#         two_trapezoid_area = h/2 * (f(a) + f(mid)) / 2.0 + &
#                                 h/2 * (f(mid) + f(b)) / 2.0
#         if (abs(one_trapezoid_area - two_trapezoid_area) < 3.0 * tolerance) then
#             integral_result = two_trapezoid_area
#         else
#             left_area = integral (f, a, mid, tolerance / 2)
#             right_area = integral (f, mid, b, tolerance / 2)
#             integral_result = left_area + right_area
#         end if
# 
#     end function integral
# 
# end module integral_module
# 
# program integrate
# 
#     use function_module
#     use integral_module
#     use math_module, only : pi
#     implicit none
# 
#     real        :: x_min, x_max
#     real        :: answer
# 
#     x_min = -4.0
#     x_max = 4.0
#     answer = integral(f, x_min, x_max, tolerance = 0.01)
#     write (*, '(a, f5.1, a, f5.1, a)') & 
#         "This program computes the integral of e^(-x^2) from ", &
#         x_min, " to ", x_max, " using adaptive numerical integration."
#     print *
#     write (*, '(a, f11.6)') "The integral is approximately ", answer
#     write (*, '(a, f11.6)') "The exact answer is ", sqrt(pi)
# 
# end program integrate
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_3_17_Case_Study__Adaptive_Numerical_Integration"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")

