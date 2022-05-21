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
# # Section 3.4: Putting Procedures in a Module

# Adapted from: "Guide to Fortran 2008 Programming" by Walter S. Brainerd (Springer 2015)

# ## Program that demonstrates putting procedures into a module.

# ```fortran
# module sort_3_module
# 
#     implicit none
#     private
#     real :: n1, n2, n3
# 
#     public ::   read_the_numbers, &
#                 sort_the_numbers, &
#                 print_the_numbers
# 
#     private swap
# 
# contains
# 
#     subroutine swap(a, b)
#         real, intent(in out) :: a, b
#         real temp
#         temp = a
#         a = b
#         b = temp
#     end subroutine swap
# 
#     subroutine read_the_numbers()
#         !print *, "Enter three numbers separated by spaces:"
#         read *, n1, n2, n3
#         write (*, '(a, f20.3)') "Input data n1:", n1
#         write (*, '(a, f20.3)') "Input data n2:", n2
#         write (*, '(a, f20.3)') "Input data n3:", n3
#    end subroutine read_the_numbers
# 
#    subroutine sort_the_numbers()
#         if (n1 > n2) then
#             call swap(n1, n2)
#         end if
#         if (n1 > n3) then
#             call swap(n1, n3)
#         end if
#         if (n2 > n3) then
#             call swap(n2, n3)
#         end if
#     end subroutine sort_the_numbers
# 
#     subroutine print_the_numbers()
#         write (*, '(a)') "The numbers, in ascending order, are:"
#         write (*, '(3f20.3)') n1, n2, n3
#     end subroutine print_the_numbers
# 
# end module sort_3_module
# 
# program sort_3
# 
#     use sort_3_module
#     implicit none
# 
#     call read_the_numbers()
#     call sort_the_numbers()
#     call print_the_numbers()
# 
# end program sort_3
# ```

# The above program is compiled and run using Fortran Package Manager (fpm):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_3_4_Putting_Procedures_in_a_Module"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_status = os.system("fpm build > /dev/null")


# fpm run output is piped into sed to suppress the status of the run command and only print the output of the executable.

# In[5]:


exec_status = os.system("echo '819.234 122381.899 1718.9787' | fpm run | sed 1,1d")

