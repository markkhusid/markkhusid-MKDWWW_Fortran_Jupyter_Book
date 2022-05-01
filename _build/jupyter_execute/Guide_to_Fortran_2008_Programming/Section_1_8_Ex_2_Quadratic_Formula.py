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
# # Section 1.8 Example 2: Quadratic Equation

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program to compute the roots of a quadratic Equation using the quadratic formula

# ```fortran
# program quadratic_equation_solver
# 
# ! Calculates and prints the roots
# ! of a quadratic equation
# 
#     implicit none
# 
#     ! Variables
#     !   a, b, c: coefficients
#     !   x1, x2: roots
# 
#     real            :: a, b, c, x1, x2, x1_smaller, x2_smaller
#     real            :: difference, percentage
#     complex         :: z1, z2
# 
#     real            :: discriminant
# 
#     print *
#     write (*, '(a)') "***** Quadratic Equation Solver *****"
#     print *
# 
#     ! For the Jupyter Notebook, we will pipe the coefficients from the command line 
#     ! Read the coefficients
#     !print *, "Enter a, the coefficient of x ** 2 -->"
#     !read *, a
# 
#     !print *, "Enter b, the coefficient of x -->"
#     !read *, b
# 
#     !print *, "Enter c, the constant term -->"
#     !read *, c
#     
#     ! The piped output from an echo statement will be processed by the line below
#     read *, a, b, c
#     
#     write (*, '(a)') "The read in coefficients are:"
#     write (*, '(3 (a, f8.3))') "a = ", a, "   b = ", b, "   c = ", c
#     print * ! skip a line on the screen
# 
#     if (a == 1) then
#         write (*, '(a, f6.3, a, f5.3)' ) "This program will solve the quadratic equation x^2 ", b, "x + ", + c
#     else if ((a /= 1) .and. (b > 0)) then
#         write (*, '(a, f5.3, a, f6.3, a, f5.3)') "This program will solve the quadratic equation ", a, "x^2 +", b, "x + ", c
#     else if ((a /= 1) .and. (b < 0)) then
#         write (*, '(a, f5.3, a, f6.3, a, f5.3)') "This program will sovle the quadratic equation ", a, "x^2 ", b, "x + ", c
#     end if
# 
#     print * ! skip a line on the screen
# 
#     if ((a == 0) .and. (b == 0)) then
#         ! Handle impossible case a and b both equal to zero
#         write (*, '(a)') "Coefficients of a and b cannot both be zero!"
#     else if ((a == 0) .and. (b /= 0)) then
#         ! Handle linear case
#         x1 = -c / b
#         x2 = x1
# 
#         ! Print the roots
#         write (*, '(a)') "Linear case: the root is:"
#         write (*, '(a)') "x = ", x1
# 
#     else if ((a /= 0) .and. (b /= 0)) then
#         ! Handle 2nd order cases by first calculating the discriminant
#         !print * ! kips a line on the screen
#         discriminant = ((b ** 2) - (4 * a * c))
#         write (*, '(a, f8.3)') "The discriminant = ", discriminant
#         print * ! skip a line on the screen
# 
#         if (discriminant > 0) then
#         ! Calculate real, non-degenerate roots by the quadratic formula
# 
#             write (*, '(a)') "Roots are real and non-degenerate..."
#             x1 = (-b + sqrt(discriminant)) / (2 * a)
#             x2 = (-b - sqrt(discriminant)) / (2 * a)
#         
#         else if (discriminant == 0) then
#         ! Calculate real, degenerate roots by the quadratic formula
#             write (*, '(a)') "Roots are real and degenerate..."
#             x1 = (-b + sqrt(discriminant)) / (2 * a)
#             x2 = x1
# 
#         else if (discriminant < 0) then
#             write (*, '(a)') "Roots are complex"
#             x1 = 0
#             x2 = 0
#             z1 = (-b + sqrt (cmplx (discriminant))) / (2 * a)
#             z2 = (-b - sqrt (cmplx (discriminant))) / (2 * a)
# 
#         end if
# 
#         ! Calculate the smaller root using x1 = c / (a * x2) and taking abs value
#         if (abs(x1) < abs(x2)) then
#             x1_smaller = abs(c / (a * x2))
#             difference = abs(x1)- x1_smaller
#             percentage = (difference / x1_smaller) * 100
#         else if (abs(x1) > abs(x2)) then
#             x2_smaller = abs(c / (a * x1))
#             difference = abs(x2) - x2_smaller
#             percentage = (difference / x2_smaller) * 100
#         else if (abs(x1) == abs(x2)) then
#             x1_smaller = abs (c / (a * x2))
#             x2_smaller = x1_smaller
#             difference = 0
#             percentage = 0
#         end if
# 
#         ! Print the roots
#         if (discriminant >= 0) then
#             print * ! skip a line on the screen
#             write (*, '(a)')  "The roots are (using just sqrt):"
#             write (*, '(a, f6.3)') "x1 = ", x1
#             write (*, '(a, f6.3)') "x2 = ", x2
#             print * ! skip a line on the screen
#             ! ************
# 
#             ! ************
#             write (*, '(a)') "The absolute value of the smaller root according to x2 = c/ax1 is:"
# 
#             if (abs(x1) <= abs(x2)) then
#                 write (*, '(a, f5.3)') "x1 = ", x1_smaller
#             else if (abs(x1) >= abs(x2)) then
#                 write (*, '(a, f5.3)') "x2 = ", x2_smaller
#             end if
# 
#             ! ************
#             print * ! skip a line on the screen
#             write (*, '(a, f5.3)') "The difference is: ", difference
#             write (*, '(a, f5.3, a)') "The percentage difference is: ", percentage, "%"
# 
#             ! ************
#         else if (discriminant < 0) then
#             print * ! skip a line on the screen
#             write (*, '(a)') "The roots are (using sqrt and cmplx):"
#             write (*, '(a, f6.3, a, f5.3, a)') "z1 = ", real(z1), " +", aimag(z1), "i"
#             write (*, '(a, f6.3, a, f6.3, a)') "z2 = ", real(z2), " ",  aimag(z2), "i"
#         end if
#     end if
# 
#  end program quadratic_equation_solver
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_1_8_Ex_2_Quadratic_Formula"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# ### Find the roots for the equation <br>
# $$
# \Large x^2 + 3x + 2 = 0
# $$

# In[5]:


exec_status = os.system("echo '1 3 2' | fpm run | sed 1,1d")


# ### Find the roots for the equation <br>
# $$
# \Large x^2 + 2x + 1 = 0
# $$

# In[6]:


exec_status = os.system("echo '1 2 1' | fpm run | sed 1,1d")


# ### Find the roots for the equation <br>
# $$
# \Large x^2 + 5x + 9 = 0
# $$

# In[7]:


exec_status = os.system("echo '1 5 9' | fpm run | sed 1,1d")


# ### Find the roots for the equation <br>
# $$
# \Large x^2 + 6x + 1 = 0
# $$

# In[8]:


exec_status = os.system("echo '1 6 1' | fpm run | sed 1,1d")

