program max_array
    implicit none
    integer, dimension(3, 4) :: A
    integer :: i, j
    character(len=10), parameter :: FMT = '(A, 4I13)'

    A = reshape (  [ &
                    ( &
                      ((i - 1)*size(A, 2) + j, &
                        j=1,size(A, 2)), &
                        i=1,size(A, 1) &
                    ) &
                  ], &
                  shape(A) &
                ) - 8

    ! Print out array
    do i = 1, size(A, 1)
        print *, A(i, :)
    end do

    print *

    print FMT, 'maximum =                       ', maxval(A)
    print FMT, 'row maximum =                   ', maxval(A, dim=1)
    print FMT, 'column maximum =                ', maxval(A, dim=2)
    print FMT, 'maximum odd elment =            ', maxval(A, mask=mod(A, 2) /= 0)
    print FMT, 'row maximum negative element =  ', maxval(A, dim=2, mask=A < 0)
    print FMT, 'maxloc (row, col) =             ', maxloc(A)
    print FMT, 'column maxloc (columns) =       ', maxloc(A, dim=2)
end program max_array
