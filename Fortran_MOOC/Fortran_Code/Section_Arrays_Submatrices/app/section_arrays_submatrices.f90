program submatrices
  implicit none
  integer, dimension(3, 4) :: A
  integer, dimension(12)   :: A_array
  integer :: i, j

  A_array = [ (((i - 1)*size(A, 2) + j, &
                   j=1, size(A, 2)), &
                   i=1, size(A, 1)) ]

  A = reshape([ (((i - 1)*size(A, 2) + j, &
                   j=1, size(A, 2)), &
                   i=1, size(A, 1)) ], &
              shape(A))
              
  
  print *, "A_array contains: ", A_array

  print *, "A matrix contains: "
  
  do i = 1, size(A, 1)
    print *, A(i, :)
  end do

  print *
  print *, "Row 2 contains: "
  print *, A(2, :)
  print *, "Column 3 contains: "
  print *, A(:, 3)
  print '(A, I0)', 'rank = ', rank(A(2, :))
  print '(A, I0)', 'shape = ', shape(A(2, :))
end program submatrices