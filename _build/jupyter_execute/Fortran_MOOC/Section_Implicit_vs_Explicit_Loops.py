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
# # Section: Implicit vs. Explicit Loops
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/implicit_loops](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/implicit_loops)

# ## This program demonstrates the speed of implicit vs. explicit loops in Fortran.

# The program will take in a command line argument and construct two argument X argument sized matrices composed of random numbers.  The program will then compute the following:

# $$
# \Large Result = \sum \sqrt{X^2 + Y^2}
# $$
# where: <br>
# $Result$ is the summation result <br>
# $X$ and $Y$ are command line argument X command line argument sized matrices

# ```fortran
# program real32_vs_real64
#     use, intrinsic :: iso_fortran_env, only : error_unit, I8 => INT64, &
#         SP => REAL32, DP => REAL64
#     implicit none
#     integer(kind=I8) :: nr_values
#     real(kind=SP), dimension(:), allocatable :: x_sp, y_sp
#     real(kind=SP) :: result
#     real :: start_time, end_time
#     integer :: status, i
# 
#     call get_argument(nr_values)
# 
#     ! implicit loops
#     allocate (x_sp(nr_values), y_sp(nr_values), stat=status)
#     if (status /= 0) then
#         write (unit=error_unit, fmt='(A)') 'error: can not allocate x_sp/y_sp'
#         stop 1
#     end if
#     call random_number(x_sp)
#     call random_number(y_sp)
# 
#     call cpu_time(start_time)
#     result = sum(sqrt(x_sp**2 + y_sp**2))
#     call cpu_time(end_time)
#     print '(A, F20.8)', 'Implicit loop time [s]: ', end_time - start_time
#     print '(A, F20.8)', 'Summation result: ', result
#     deallocate (x_sp, y_sp)
# 
#     ! explicit loops
#     allocate (x_sp(nr_values), y_sp(nr_values), stat=status)
#     if (status /= 0) then
#         write (unit=error_unit, fmt='(A)') 'error: can not allocate x_sp/y_sp'
#         stop 1
#     end if
#     call random_number(x_sp)
#     call random_number(y_sp)
# 
#     call cpu_time(start_time)
#     result = 0.0_SP
#     do i = 1, size(x_sp)
#         result = result + sqrt(x_sp(i)**2 + y_sp(i)**2)
#     end do
#     call cpu_time(end_time)
#     print '(A, F20.8)', 'Explicit loop time [s]: ', end_time - start_time
#     print '(A, F20.8)', 'Summation result: ', result
#     deallocate (x_sp, y_sp)
# 
# contains
# 
#     subroutine get_argument(nr_values)
#         implicit none
#         integer(Kind=I8), intent(out) :: nr_values
#         character(len=1024) :: buffer, msg
#         integer :: status
# 
#         if (command_argument_count() /= 1) then
#             write (unit=error_unit, fmt='(A)') 'error: expect number of values'
#             stop 2
#         end if
#         call get_command_argument(1, buffer)
#         read (buffer, fmt=*, iomsg=msg, iostat=status) nr_values
#         if (status /= 0) then
#             write (unit=error_unit, fmt='(2A)') 'error: ', trim(msg)
#             stop 3
#         end if
#     end subroutine get_argument
# 
# end program real32_vs_real64

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Implicit_vs_Explicit_Loops"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', "%%writefile section_implicit_vs_explicit_loops.f90\nprogram real32_vs_real64\n    use, intrinsic :: iso_fortran_env, only : error_unit, I8 => INT64, &\n        SP => REAL32, DP => REAL64\n    implicit none\n    integer(kind=I8) :: nr_values\n    real(kind=SP), dimension(:), allocatable :: x_sp, y_sp\n    real(kind=SP) :: result\n    real :: start_time, end_time\n    integer :: status, i\n\n    call get_argument(nr_values)\n\n    ! implicit loops\n    allocate (x_sp(nr_values), y_sp(nr_values), stat=status)\n    if (status /= 0) then\n        write (unit=error_unit, fmt='(A)') 'error: can not allocate x_sp/y_sp'\n        stop 1\n    end if\n    call random_number(x_sp)\n    call random_number(y_sp)\n\n    call cpu_time(start_time)\n    result = sum(sqrt(x_sp**2 + y_sp**2))\n    call cpu_time(end_time)\n    print '(A, F20.8)', 'Implicit loop time [s]: ', end_time - start_time\n    print '(A, F20.8)', 'Summation result: ', result\n    deallocate (x_sp, y_sp)\n\n    ! explicit loops\n    allocate (x_sp(nr_values), y_sp(nr_values), stat=status)\n    if (status /= 0) then\n        write (unit=error_unit, fmt='(A)') 'error: can not allocate x_sp/y_sp'\n        stop 1\n    end if\n    call random_number(x_sp)\n    call random_number(y_sp)\n\n    call cpu_time(start_time)\n    result = 0.0_SP\n    do i = 1, size(x_sp)\n        result = result + sqrt(x_sp(i)**2 + y_sp(i)**2)\n    end do\n    call cpu_time(end_time)\n    print '(A, F20.8)', 'Explicit loop time [s]: ', end_time - start_time\n    print '(A, F20.8)', 'Summation result: ', result\n    deallocate (x_sp, y_sp)\n\ncontains\n\n    subroutine get_argument(nr_values)\n        implicit none\n        integer(Kind=I8), intent(out) :: nr_values\n        character(len=1024) :: buffer, msg\n        integer :: status\n\n        if (command_argument_count() /= 1) then\n            write (unit=error_unit, fmt='(A)') 'error: expect number of values'\n            stop 2\n        end if\n        call get_command_argument(1, buffer)\n        read (buffer, fmt=*, iomsg=msg, iostat=status) nr_values\n        if (status /= 0) then\n            write (unit=error_unit, fmt='(2A)') 'error: ', trim(msg)\n            stop 3\n        end if\n    end subroutine get_argument\n\nend program real32_vs_real64")


# In[6]:


get_ipython().system('bat *.f90')


# In[7]:


os.chdir(code_dir)


# In[8]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[9]:


exec_status = os.system("fpm run -- 10 2>/dev/null")


# In[10]:


exec_status = os.system("fpm run -- 100 2>/dev/null")


# In[11]:


exec_status = os.system("fpm run -- 1000 2>/dev/null")


# In[12]:


exec_status = os.system("fpm run -- 10000 2>/dev/null")


# In[13]:


exec_status = os.system("fpm run -- 100000 2>/dev/null")


# In[14]:


exec_status = os.system("fpm run -- 1000000 2>/dev/null")


# In[15]:


exec_status = os.system("fpm run -- 10000000 2>/dev/null")


# In[16]:


exec_status = os.system("fpm run -- 100000000 2>/dev/null")

