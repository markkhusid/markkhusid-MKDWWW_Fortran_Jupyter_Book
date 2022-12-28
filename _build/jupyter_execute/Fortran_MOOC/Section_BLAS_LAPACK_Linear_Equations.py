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
# # Section: BLAS/LAPACK - Linear Equations
# 

# Adapted from: [https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack/linear_equations](https://github.com/gjbex/Fortran-MOOC/tree/master/source_code/blas_lapack/linear_equations)

# ## This program demonstrates solving linear algebra equations in Fortran.

# ### Linear Equation Problem

# In this notebook we will use Fortran to solve a system of linear equations of the form:

# $$
# \Large A \mathbf{x} = \mathbf{b}
# $$
# where: <br>
# 

# $$
# \Large A =
# \left[
# \begin{array}{cccc}
# a_{11} & a_{12} & \cdots & a_{1n} \\
# a_{21} & a_{22} & \cdots & a_{2n} \\
# \vdots & \vdots & \vdots & \vdots \\
# a_{m1} & a_{m2} & \cdots & a_{mn}
# \end{array}
# \right]
# $$

# $$
# \Large \mathbf{x} =
# \left[
# \begin{array}{c}
# x_{1}  \\
# x_{2}  \\
# \vdots \\
# x_{n}
# \end{array}
# \right]
# $$

# $$
# \Large \mathbf{b} = 
# \left[
# \begin{array}{c}
# b_{1}  \\
# b_{2}  \\
# \vdots \\
# b_{n}
# \end{array}
# \right]
# $$

# The approach will be to have a main program that reads in as parameters the number of equations, the matrix $\mathbf{A}$ and the vector $\mathbf{x}$ as text files.  The main program is called *solve_equations.f90*.  It makes use of the LAPACK linear equation solver routine called **DGESV**.  Information on this routine can be found at [LAPACK - DGESV](https://netlib.org/lapack/explore-html/d7/d3b/group__double_g_esolve_ga5ee879032a8365897c3ba91e3dc8d512.html#ga5ee879032a8365897c3ba91e3dc8d512).
# 
# The main program makes use of a module called *linalg_mod.f90*, which contains subroutines to read and write matrices and arrays to and from text files.
# 
# Finally, there is a helper program called *generate_array.f90* which has a subroutine that gets arguments from the command line and generates either of vector or matrix of specified size.  Every element in the array or matrix is a random number.
# 
# The individual program files are listed below:

# ### In file linalg_mod.f90

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Linear_Equations/src/linalg_mod.f90
# ---
# language: fortran
# ---
# ```

# ### In file generate_array.f90

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Linear_Equations/app/generate_array.f90
# ---
# language: fortran
# ---
# ```

# ### In solve_equations.f90

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Linear_Equations/app/solve_equations.f90
# ---
# language: fortran
# ---
# ```

# The above programs are compiled and run using Fortran Package Manager (fpm):

# ## Build the Program using FPM (Fortran Package Manager)

# In[1]:


import os
root_dir = ""
root_dir = os.getcwd()


# Since the code makes use of the LAPACK library, the following FPM configuration file (fpm.toml) was used:

# ```{literalinclude} Fortran_Code/Section_BLAS_LAPACK_Linear_Equations/fpm.toml
# ---
# language: toml
# ---
# ```

# In[2]:


code_dir = root_dir + "/" + "Fortran_Code/Section_BLAS_LAPACK_Linear_Equations"


# In[3]:


os.chdir(code_dir)


# The files *solve_equations.f90* and *generate_array.f90* were placed into the "app" folder, while the file *linalg_mod.f90* was placed into the "src" folder.

# In[4]:


build_status = os.system("fpm build 2>/dev/null")


# ## Run the Program using FPM (Fortran Package Manager)

# ### Solve a Test Linear System of Two Equations

# As our first run, we wish to solve the following set of linear equations:

# $$
# \begin{align*}
# 2x+8y & = 20 \\
# x+2y  & = 4
# \end{align*}
# $$

# The variables in the equations are converted into components of the $\mathbf{x}$ vector as shown below:

# $$
# \begin{align*}
# 2x_1+8x_2 & = 20 \\
# x_1+2x_2  & = 4
# \end{align*}
# $$

# These equations are converted into matrix form as shown below:

# $$
# \begin{equation*}
# \left[
# \begin{array}{cc}
# 2 & 8 \\
# 1 & 2 \\
# \end{array}
# \right]
# \left[
# \begin{array}{c}
# x_1 \\
# x_2 \\
# \end{array}
# \right]
# =
# \left[
# \begin{array}{c}
# 20 \\
# 4 \\
# \end{array}
# \right]
# \end{equation*}
# $$

# Therefore we have the following:

# $$
# \mathbf{A} = 
# \left[
# \begin{array}{cc}
# 2 & 8 \\
# 1 & 2 
# \end{array}
# \right]
# $$

# $$
# \mathbf{x} = 
# \left[
# \begin{array}{c}
# x_1 \\
# x_2  
# \end{array}
# \right]
# $$

# 
# $$
# \mathbf{b} = 
# \left[
# \begin{array}{c}
# 20 \\
# 4  
# \end{array}
# \right]
# $$
# 

# The matrix $\mathbf{A}$ and the vector $\mathbf{b}$ are written into text files as shown below:

# In[5]:


get_ipython().run_cell_magic('writefile', 'A_test1.txt', '2 8\n1 2')


# In[6]:


get_ipython().run_cell_magic('writefile', 'b_test1.txt', '20\n4')


# The *solve_equations* program can now be run with the number of equations command line argument set to 2, and the files *A_test1.txt* and *b_test1.txt*

# In[7]:


exec_status =     os.system("fpm run solve_equations 2>/dev/null -- 2 A_test1.txt b_test1.txt")


# The results are printed in scientfic notation and in the order of $x_1$, $x_2$.

# We now wish to use Python's Numpy library to test these results:

# In[8]:


import numpy as np

A = np.genfromtxt("A_test1.txt")
b = np.genfromtxt("b_test1.txt")
x = np.linalg.solve(A, b)
print("x1 = {0:2.1f}".format(x[0]))
print("x2 = {0:2.1f}".format(x[1]))


# We can see that the Fortran code and Numpy produce the same results.

# ### Solve a Test Linear System of Equations of Arbitrary Size

# The Fortran code can be used to solve an arbitrarily large system of equations.  To test this functionality, we make use of the *generate_array.f90* program to generate arrays or matrices of arbitrary size filled with random numbers.
# 
# As a start, we will use the *generate_array.f90* to generate a matrix file A_test2.txt that contains a 10x10 matrix.

# In[9]:


exec_status = os.system("fpm run generate_array 2>/dev/null -- 10 10 > A_test2.txt") 


# The $\mathbf{A}$ matrix is shown below:

# In[10]:


import pandas as pd
A = pd.read_table("A_test2.txt", 
    header=None, 
    sep='\s+')
A


# And now we generate the $\mathbf{b}$ vector:

# In[11]:


exec_status = os.system("fpm run generate_array 2>/dev/null -- 10 > b_test2.txt") 


# The $\mathbf{b}$ vector is shown below:

# In[12]:


b = pd.read_table("b_test2.txt", 
    header=None, 
    sep='\s+')
b


# We now use the *solve_equation* Fortran code to solve this linear system of equations:

# In[13]:


exec_status =     os.system("fpm run solve_equations 2>/dev/null -- 10 A_test2.txt b_test2.txt")


# And the results are compared to the output of Numpy:

# In[14]:


A = np.genfromtxt("A_test2.txt")
b = np.genfromtxt("b_test2.txt")
x = np.linalg.solve(A, b)

for i in range(len(x)):
    print ("x{0:d} = {1:2.6f}".format(i+1, x[i]))


# Again, we see that the results are the same.
