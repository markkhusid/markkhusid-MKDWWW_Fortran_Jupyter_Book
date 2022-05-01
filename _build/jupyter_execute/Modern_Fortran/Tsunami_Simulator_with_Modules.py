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
# # Tsunami Simulator with Modules

# Adapted from: "Modern Fortan" by Milan Curcic (Manning)

# In this section the Tsunami Simulator is rewritten using Fortran Modules.

# ## The file mod_inital.f08 contains:

# ```fortran
# module mod_initial
#     
#     private
#     public :: set_gaussian
# 
# contains
#     
#     pure subroutine set_gaussian(x, icenter, decay)
#         real, intent(in out) :: x(:)
#         integer, intent(in)  :: icenter
#         real, intent(in)     :: decay
#         
#         integer :: i
#     
#         do concurrent(i = 1:size(x))
#             x(i) = exp(-decay * (i - icenter)**2)
#         end do
#     end subroutine set_gaussian
#     
# end module mod_initial
# ```

# ## The file mod_diff.f08 contains:

# ```fortran
# module mod_diff
# 
#     use iso_fortran_env, only: int32, real32
#     implicit none
#     
#     private
#     public :: diff_upwind, diff_centered
#     
# contains
# 
#     pure function diff_upwind(x) result(dx)
#         real(real32), intent(in) :: x(:)
#         real(real32)             :: dx(size(x))
#         integer(int32)           :: im
#         
#         im       = size(x)
#         dx(1)    = x(1) - x(im)
#         dx(2:im) = x(2:im) - x(1:im - 1)
#     end function diff_upwind
#     
#     pure function diff_centered(x) result(dx)
#         real(real32), intent(in) :: x(:)
#         real(real32)             :: dx(size(x))
#         integer(int32)           :: im
#         
#         im         = size(x)
#         dx(1)      = x(2) - x(im)
#         dx(im)     = x(1) - x(im - 1)
#         dx(2:im-1) = x(3:im) - x(1:im-2)
#     end function diff_centered
#     
# end module mod_diff
# ```

# ## Main Program

# ```fortran
# program tsunami_simulator_with_modules
# 
#     use iso_fortran_env, only : int32, real32
#     use mod_diff, only        : diff => diff_centered
#     use mod_initial, only     : set_gaussian
#     
#     implicit none
#     
#     integer(int32) :: n
#     
#     integer(int32), parameter :: grid_size = 100
#     integer(int32), parameter :: num_time_steps = 5000
#     real(real32),   parameter :: dt = 0.02, dx = 1, g = 9.8
#     real(real32),   parameter :: hmean = 10
#     
#     real(real32)              :: h(grid_size), u(grid_size)
#     
#     integer(int32), parameter :: icenter = 25
#     real(real32), parameter   :: decay = 0.02
#     
#     logical :: file_exists
#     
#     open(9, file = 'tsunami_simulator_with_modules_data.txt')
#     
#     if (grid_size <= 0) stop 'grid_size must be > 0'
#     if (dt <= 0) stop 'time step dt must be > 0'
#     if (dx <= 0) stop 'grid spacing dx must be > 0'
#     
#     call set_gaussian(h, icenter, decay)
#     u = 0
#     
#     !print *, 0, h
#     write (9, *) 0, h
#     close(9)
#     
#     time_loop: do n = 1, num_time_steps
#         
#         u = u - (u * diff(u) + g * diff(h)) / dx * dt
#         h = h - diff(u * (hmean + h)) / dx * dt
#         
#         !print *, n, h
#         
#         inquire(file = 'tsunami_simulator_with_modules_data.txt', exist = file_exists)
#         if (file_exists) then
#             open(9, file = 'tsunami_simulator_with_modules_data.txt', status = 'old', position = 'append', action = 'write')
#         else
#             open(9, file = 'tsunami_simulator_with_modules_data.txt', status = "new", action = 'write')
#         end if
#         
#         write (9, *) n, h
# 
#     end do time_loop
#      
#     close(9)
#     
# end program tsunami_simulator_with_modules
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Tsunami_Simulator_with_Modules"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command.

# In[5]:


exec_status = os.system("fpm run | sed 1,1d")


# The above Fortran code writes the calculations to a file called **tsunami_simulator_with_modules_data.txt**

# In[6]:


import pandas as pd
output_filename = 'tsunami_simulator_with_modules_data.txt'
data_file = code_dir + "/" + output_filename
table = pd.read_fwf(data_file, header=None)
table

