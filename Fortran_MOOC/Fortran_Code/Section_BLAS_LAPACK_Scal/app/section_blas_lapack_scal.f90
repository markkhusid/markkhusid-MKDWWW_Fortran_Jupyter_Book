program scal
  use, intrinsic :: iso_fortran_env, only : error_unit, DP => REAL64
  implicit none
  integer, parameter :: rows = 3, cols = 4
  real(kind=DP), dimension(rows, cols) :: matrix
  real(kind=DP), dimension(rows) :: norm
  integer :: row

  ! Define the explicit interface for the BLAS subroutine dscal
  interface
      subroutine dscal(n, da, dx, incx)
          import :: DP
          integer :: n, incx
          real(kind=DP) :: da
          real(kind=DP), dimension(*) :: dx
      end subroutine dscal
  end interface

  ! Initialize matrix with random numbers
  call random_number(matrix)
  
  ! Print original matrix
  print '(A)', 'original:'

  ! Print matrix
  call print_matrix(matrix)

  ! Normalize along each column
  norm = sum(matrix, dim=2)
  print '(A, *(F12.7))', 'norm:', norm

  ! Loop over rows
  do row = 1, rows
      print '(A, I0)', 'row: ', row
      print '(A, F12.7)', '1/norm(row): ', 1.0_DP/norm(row)

      ! In Fortran, the function call for dscal is:
      ! call dscal(n, da, dx, incx)
      ! where:
      ! n is the number of elements in the vector
      ! da is the scalar
      ! dx is the vector
      ! incx is the increment between elements of the vector
      call dscal(cols, 1.0_DP/norm(row), matrix(row, :), 1)
      
      ! Print the matrix
      call print_matrix(matrix)
  end do
  print '(A)', 'row-normalized::'
  ! Print matrix
  call print_matrix(matrix)

  ! Normalize along each column
  norm = sum(matrix, dim=2)
  print '(A, *(F12.7))', 'norm:', norm

contains

  subroutine print_matrix(matrix)
      implicit none
      real(kind=DP), dimension(:, :), intent(in) :: matrix
      integer :: row

      do row = 1, size(matrix, 1)
          print '(*(F12.7))', matrix(row, :)
      end do
  end subroutine print_matrix

end program scal
