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
# # Section: Ball Throw
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/ball_throw](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/ball_throw)

# ## This program demonstrates simulating a ball throw in Fortran.

# ### In rk4.f90

# ```fortran
# module rk4_mod
# 
#     public :: rk4, rk4vec
# 
# contains
# 
# subroutine rk4 ( t0, u0, dt, f, u )
# 
# !*****************************************************************************80
# !
# !! RK4 takes one Runge-Kutta step for a scalar ODE.
# !
# !  Discussion:
# !
# !    It is assumed that an initial value problem, of the form
# !
# !      du/dt = f ( t, u )
# !      u(t0) = u0
# !
# !    is being solved.
# !
# !    If the user can supply current values of t, u, a stepsize dt, and a
# !    function to evaluate the derivative, this function can compute the
# !    fourth-order Runge Kutta estimate to the solution at time t+dt.
# !
# !  Licensing:
# !
# !    This code is distributed under the GNU LGPL license. 
# !
# !  Modified:
# !
# !    31 January 2012
# !
# !  Author:
# !
# !    John Burkardt
# !
# !  Parameters:
# !
# !    Input, real ( kind = 8 ) T0, the current time.
# !
# !    Input, real ( kind = 8 ) U0, the solution estimate at the current time.
# !
# !    Input, real ( kind = 8 ) DT, the time step.
# !
# !    Input, external F, a subroutine of the form 
# !      subroutine f ( t, u, uprime ) 
# !    which evaluates the derivative uprime given the time T and
# !    solution vector U.
# !
# !    Output, real ( kind = 8 ) U, the fourth-order Runge-Kutta solution 
# !    estimate at time T0+DT.
# !
#   implicit none
# 
#   real ( kind = 8 ) dt
#   external f
#   real ( kind = 8 ) f0
#   real ( kind = 8 ) f1
#   real ( kind = 8 ) f2
#   real ( kind = 8 ) f3
#   real ( kind = 8 ) t0
#   real ( kind = 8 ) t1
#   real ( kind = 8 ) t2
#   real ( kind = 8 ) t3
#   real ( kind = 8 ) u
#   real ( kind = 8 ) u0
#   real ( kind = 8 ) u1
#   real ( kind = 8 ) u2
#   real ( kind = 8 ) u3
# !
# !  Get four sample values of the derivative.
# !
#   call f ( t0, u0, f0 )
# 
#   t1 = t0 + dt / 2.0D+00
#   u1 = u0 + dt * f0 / 2.0D+00
#   call f ( t1, u1, f1 )
# 
#   t2 = t0 + dt / 2.0D+00
#   u2 = u0 + dt * f1 / 2.0D+00
#   call f ( t2, u2, f2 )
# 
#   t3 = t0 + dt
#   u3 = u0 + dt * f2
#   call f ( t3, u3, f3 )
# !
# !  Combine them to estimate the solution U at time T1.
# !
#   u = u0 + dt * ( f0 + 2.0D+00 * f1 + 2.0D+00 * f2 + f3 ) / 6.0D+00
# 
#   return
# end
# subroutine rk4vec ( t0, m, u0, dt, f, u )
# 
# !*****************************************************************************80
# !
# !! RK4VEC takes one Runge-Kutta step for a vector ODE.
# !
# !  Discussion:
# !
# !    Thanks  to Dante Bolatti for correcting the final function call to:
# !      call f ( t3, m, u3, f3 )
# !    18 August 2016.
# !
# !  Licensing:
# !
# !    This code is distributed under the GNU LGPL license. 
# !
# !  Modified:
# !
# !    18 August 2016
# !
# !  Author:
# !
# !    John Burkardt
# !
# !  Parameters:
# !
# !    Input, real ( kind = 8 ) T0, the current time.
# !
# !    Input, integer ( kind = 4 ) M, the dimension of the system.
# !
# !    Input, real ( kind = 8 ) U0(M), the solution estimate at the current time.
# !
# !    Input, real ( kind = 8 ) DT, the time step.
# !
# !    Input, external F, a subroutine of the form 
# !      subroutine f ( t, m, u, uprime ) 
# !    which evaluates the derivative UPRIME(1:M) given the time T and
# !    solution vector U(1:M).
# !
# !    Output, real ( kind = 8 ) U(M), the fourth-order Runge-Kutta solution 
# !    estimate at time T0+DT.
# !
#   implicit none
# 
#   integer ( kind = 4 ) m
# 
#   real ( kind = 8 ) dt
#   external f
#   real ( kind = 8 ) f0(m)
#   real ( kind = 8 ) f1(m)
#   real ( kind = 8 ) f2(m)
#   real ( kind = 8 ) f3(m)
#   real ( kind = 8 ) t0
#   real ( kind = 8 ) t1
#   real ( kind = 8 ) t2
#   real ( kind = 8 ) t3
#   real ( kind = 8 ) u(m)
#   real ( kind = 8 ) u0(m)
#   real ( kind = 8 ) u1(m)
#   real ( kind = 8 ) u2(m)
#   real ( kind = 8 ) u3(m)
# !
# !  Get four sample values of the derivative.
# !
#   call f ( t0, m, u0, f0 )
# 
#   t1 = t0 + dt / 2.0D+00
#   u1(1:m) = u0(1:m) + dt * f0(1:m) / 2.0D+00
#   call f ( t1, m, u1, f1 )
# 
#   t2 = t0 + dt / 2.0D+00
#   u2(1:m) = u0(1:m) + dt * f1(1:m) / 2.0D+00
#   call f ( t2, m, u2, f2 )
# 
#   t3 = t0 + dt
#   u3(1:m) = u0(1:m) + dt * f2(1:m)
#   call f ( t3, m, u3, f3 )
# !
# !  Combine them to estimate the solution U at time T1.
# !
#   u(1:m) = u0(1:m) + ( dt / 6.0D+00 ) * ( &
#                  f0(1:m) &
#      + 2.0D+00 * f1(1:m) &
#      + 2.0D+00 * f2(1:m) &
#      +           f3(1:m) )
# 
#   return
# end
# subroutine timestamp ( )
# 
# !*****************************************************************************80
# !
# !! TIMESTAMP prints the current YMDHMS date as a time stamp.
# !
# !  Example:
# !
# !    31 May 2001   9:45:54.872 AM
# !
# !  Licensing:
# !
# !    This code is distributed under the GNU LGPL license.
# !
# !  Modified:
# !
# !    18 May 2013
# !
# !  Author:
# !
# !    John Burkardt
# !
# !  Parameters:
# !
# !    None
# !
#   implicit none
# 
#   character ( len = 8 ) ampm
#   integer ( kind = 4 ) d
#   integer ( kind = 4 ) h
#   integer ( kind = 4 ) m
#   integer ( kind = 4 ) mm
#   character ( len = 9 ), parameter, dimension(12) :: month = (/ &
#     'January  ', 'February ', 'March    ', 'April    ', &
#     'May      ', 'June     ', 'July     ', 'August   ', &
#     'September', 'October  ', 'November ', 'December ' /)
#   integer ( kind = 4 ) n
#   integer ( kind = 4 ) s
#   integer ( kind = 4 ) values(8)
#   integer ( kind = 4 ) y
# 
#   call date_and_time ( values = values )
# 
#   y = values(1)
#   m = values(2)
#   d = values(3)
#   h = values(5)
#   n = values(6)
#   s = values(7)
#   mm = values(8)
# 
#   if ( h < 12 ) then
#     ampm = 'AM'
#   else if ( h == 12 ) then
#     if ( n == 0 .and. s == 0 ) then
#       ampm = 'Noon'
#     else
#       ampm = 'PM'
#     end if
#   else
#     h = h - 12
#     if ( h < 12 ) then
#       ampm = 'PM'
#     else if ( h == 12 ) then
#       if ( n == 0 .and. s == 0 ) then
#         ampm = 'Midnight'
#       else
#         ampm = 'AM'
#       end if
#     end if
#   end if
# 
#   write ( *, '(i2,1x,a,1x,i4,2x,i2,a1,i2.2,a1,i2.2,a1,i3.3,1x,a)' ) &
#     d, trim ( month(m) ), y, h, ':', n, ':', s, '.', mm, trim ( ampm )
# 
#   return
# end
# 
# end module rk4_mod
# ```

# ### In section_ball_throw.f90

# ```fortran
# program ball_throw
#   use, intrinsic :: iso_fortran_env, only : DP => REAL64, INT32
#   use :: rk4_mod, only  : rk4vec
#   implicit none
#   integer, parameter :: NR_EQS = 4
#   integer, parameter :: MAX_STEPS = 10000
#   real(kind=DP), parameter :: DELTA_T = 0.01_DP
#   real(kind=DP) :: t
#   real(kind=DP), dimension(NR_EQS) :: u, u_new
#   integer :: step
# 
# #define X u(1)
# #define Y u(2)
# #define VX u(3)
# #define VY u(4)
# 
#   step = 0
#   t = 0.0_DP
#   X = 0.0_DP
#   Y = 0.0_DP
#   VX = 5.0_DP
#   VY = 5.0_DP
#   print *, step, t, X, Y, VX, VY
#   do step = 1, MAX_STEPS
#       call rk4vec(t, NR_EQS, u, DELTA_T, rhs, u_new)
#       t = t + DELTA_T
#       u = u_new
#       if (Y < 0.0_DP) exit
#       print *, step, t, X, Y, VX, VY
#   end do
# 
# contains
# 
# #define X_prime  u_prime(1)
# #define Y_prime  u_prime(2)
# #define VX_prime u_prime(3)
# #define VY_prime u_prime(4)
# 
#   subroutine rhs(t, n, u, u_prime)
#       implicit none
#       real(kind=DP), intent(in) :: t
#       integer(kind=INT32) :: n
#       real(kind=DP), dimension(n), intent(in) :: u
#       real(kind=DP), dimension(n), intent(out) :: u_prime
# 
#       X_prime = VX
#       Y_prime = VY
#       VX_prime = 0.0_DP
#       VY_prime = -9.81_DP
#   end subroutine rhs
# 
# end program ball_throw
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_Ball_Throw"


# In[3]:


code_app_dir = code_dir + "/" + "app"


# In[4]:


os.chdir(code_app_dir)


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%writefile section_ball_throw.F90\nprogram ball_throw\n  use, intrinsic :: iso_fortran_env, only : DP => REAL64, INT32\n  use :: rk4_mod, only  : rk4vec\n  implicit none\n  integer, parameter :: NR_EQS = 4\n  integer, parameter :: MAX_STEPS = 10000\n  real(kind=DP), parameter :: DELTA_T = 0.01_DP\n  real(kind=DP) :: t\n  real(kind=DP), dimension(NR_EQS) :: u, u_new\n  integer :: step\n\n#define X u(1)\n#define Y u(2)\n#define VX u(3)\n#define VY u(4)\n\n  step = 0\n  t = 0.0_DP\n  X = 0.0_DP\n  Y = 0.0_DP\n  VX = 5.0_DP\n  VY = 5.0_DP\n  print *, step, t, X, Y, VX, VY\n  do step = 1, MAX_STEPS\n      call rk4vec(t, NR_EQS, u, DELTA_T, rhs, u_new)\n      t = t + DELTA_T\n      u = u_new\n      if (Y < 0.0_DP) exit\n      print *, step, t, X, Y, VX, VY\n  end do\n\ncontains\n\n#define X_prime  u_prime(1)\n#define Y_prime  u_prime(2)\n#define VX_prime u_prime(3)\n#define VY_prime u_prime(4)\n\n  subroutine rhs(t, n, u, u_prime)\n      implicit none\n      real(kind=DP), intent(in) :: t\n      integer(kind=INT32) :: n\n      real(kind=DP), dimension(n), intent(in) :: u\n      real(kind=DP), dimension(n), intent(out) :: u_prime\n\n      X_prime = VX\n      Y_prime = VY\n      VX_prime = 0.0_DP\n      VY_prime = -9.81_DP\n  end subroutine rhs\n\nend program ball_throw')


# In[6]:


get_ipython().system('bat *.F90')


# In[7]:


os.chdir(code_dir)


# In[8]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# The program is run and the output is saved into a data file *data.dat*.

# In[9]:


exec_status = os.system("fpm run > data.dat 2>/dev/null")


# ## Load *data.dat* into Pandas

# In[10]:


import pandas as pd
data = pd.read_table("data.dat", 
    header=None, 
    sep='\s+', 
    names=["step", "time", "X", "Y", "VX", "VY"])
data


# ## Plot the Height vs Time Data

# In[11]:


from bokeh.io import output_notebook
from bokeh.plotting import figure, show
output_notebook()

# create a new plot with a title and axis labels
p = figure(title="Ball Throw Plot", 
           x_axis_label="Time [s]", 
           y_axis_label="Height [arb]")

p.scatter(data.X, data.Y,
legend_label="Height [Arb]")

# show the results
show(p)

