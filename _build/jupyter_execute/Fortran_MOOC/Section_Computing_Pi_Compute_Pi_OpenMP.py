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
# # Section Computing Pi: Compute Pi with OpenMP
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/computing_pi](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/computing_pi)

# ## This program demonstrates computing $\pi$ in Fortran using OpenMP.

# ```fortran
# program compute_pi_omp
#   use, intrinsic :: iso_fortran_env, only : DP => REAL64, I8 => INT64
#   implicit none
#   integer(kind=I8) :: i, nr_iters
#   real(kind=DP) :: delta, x, pi_val
# 
#   pi_val = 0.0_DP
#   nr_iters = get_nr_iters()
#   delta = 1.0_DP/nr_iters
#   x = 0.0_DP
# 
#   !$omp parallel do default(none) private(x) shared(delta, nr_iters) reduction(+:pi_val)
#   do i = 1, nr_iters
#       x = i*delta
#       pi_val = pi_val + sqrt(1.0_DP - x**2)
#   end do
#   !$omp end parallel do
# 
#   pi_val = 4.0_DP*pi_val/nr_iters
#   print '(A, I10, A, F25.15)', "After ", nr_iters, " loops, Pi = ", pi_val
# 
# contains
#    
#   function get_nr_iters() result(nr_iters)
#       use, intrinsic :: iso_fortran_env, only : error_unit
#       implicit none
#       integer(kind=I8) :: nr_iters
#       integer(kind=I8), parameter :: default_nr_iters = 1000_I8
#       character(len=1024) :: buffer, msg
#       integer :: istat
# 
#       if (command_argument_count() >= 1) then
#           call get_command_argument(1, buffer)
#           read (buffer, fmt=*, iostat=istat, iomsg=msg) nr_iters
#           if (istat /= 0) then
#               write (unit=error_unit, fmt='(2A)') &
#                   'error: ', msg
#               stop 1
#           end if
#       else
#           nr_iters = default_nr_iters
#       end if
#   end function get_nr_iters
# 
# end program compute_pi_omp
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Computing_Pi_Compute_Pi_OpenMP"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%writefile section_computing_pi_compute_pi_openmp.f90\nprogram compute_pi_omp\n  use, intrinsic :: iso_fortran_env, only : DP => REAL64, I8 => INT64\n  implicit none\n  integer(kind=I8) :: i, nr_iters\n  real(kind=DP) :: delta, x, pi_val\n\n  pi_val = 0.0_DP\n  nr_iters = get_nr_iters()\n  delta = 1.0_DP/nr_iters\n  x = 0.0_DP\n\n  !$omp parallel do default(none) private(x) shared(delta, nr_iters) reduction(+:pi_val)\n  do i = 1, nr_iters\n      x = i*delta\n      pi_val = pi_val + sqrt(1.0_DP - x**2)\n  end do\n  !$omp end parallel do\n\n  pi_val = 4.0_DP*pi_val/nr_iters\n  print \'(A, I10, A, F25.15)\', "After ", nr_iters, " loops, Pi = ", pi_val\n\ncontains\n   \n  function get_nr_iters() result(nr_iters)\n      use, intrinsic :: iso_fortran_env, only : error_unit\n      implicit none\n      integer(kind=I8) :: nr_iters\n      integer(kind=I8), parameter :: default_nr_iters = 1000_I8\n      character(len=1024) :: buffer, msg\n      integer :: istat\n\n      if (command_argument_count() >= 1) then\n          call get_command_argument(1, buffer)\n          read (buffer, fmt=*, iostat=istat, iomsg=msg) nr_iters\n          if (istat /= 0) then\n              write (unit=error_unit, fmt=\'(2A)\') &\n                  \'error: \', msg\n              stop 1\n          end if\n      else\n          nr_iters = default_nr_iters\n      end if\n  end function get_nr_iters\n\nend program compute_pi_omp')


# In[6]:


get_ipython().system('bat *.f90')


# In[7]:


os.chdir(code_dir)


# Since this program uses the OpenMP external library, the fpm.toml file had to be augmented as below.

# In[8]:


get_ipython().system('bat fpm.toml')


# In[9]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# In[10]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 10 2>/dev/null")')


# In[11]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 100 2>/dev/null")')


# In[12]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 1000 2>/dev/null")')


# In[13]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 10000 2>/dev/null")')


# In[14]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 100000 2>/dev/null")')


# In[15]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 1000000 2>/dev/null")')


# In[16]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 10000000 2>/dev/null")')


# In[17]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 100000000 2>/dev/null")')


# In[18]:


get_ipython().run_cell_magic('timeit', '-r 10 -n 1', 'exec_status = os.system("fpm run -- 1000000000 2>/dev/null")')

