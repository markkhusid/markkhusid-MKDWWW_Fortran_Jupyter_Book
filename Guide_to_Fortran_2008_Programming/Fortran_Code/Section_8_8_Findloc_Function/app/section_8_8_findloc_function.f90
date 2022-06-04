program find_loc

    implicit none

    intrinsic :: findloc

    real, dimension (3,3)   :: X =          &
        reshape (                           &
                    [   -11,  12, -13,      &
                         21,  22, -23,      &
                         31, -32, -33 ],    &
                    [ 3, 3 ], order = [ 2, 1 ] )

    logical, parameter      :: T = .true.

    write (*,'(a)') "[*] The matrix X"
    call write_matrix(X)

    write (*,*)

    write (*,'(a)') "[*] Begin findloc call..."
    write (*,'(a)') "findloc( X > 0, T )"
    write (*,'(a, 2i2, a)')  "The first element where (i,j) > 0 is: (", &
        findloc( X > 0, T ), &
        ") in column major order."            ! = [ 2, 1 ]

    contains

        subroutine write_matrix(a)
            real, dimension(:,:), intent(in) :: a
            integer :: i, j
            do i = lbound(a,1), ubound(a,1)
                write (*,*) (a(i,j), j = lbound(a,2), ubound(a,2))
            end do
        end subroutine write_matrix

end program find_loc
