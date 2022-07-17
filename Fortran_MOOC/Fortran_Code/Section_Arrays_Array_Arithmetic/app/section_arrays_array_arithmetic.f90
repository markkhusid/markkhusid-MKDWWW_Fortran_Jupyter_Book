program array_arithmetic
    implicit none
    real, dimension(5) :: A = [ 1.2, 2.3, 3.4, 4.5, 5.6 ], &
                          B = [ -1.0, -0.5, 0.0, 0.5, 1.0], &
                          C

    print *, "The array A contains: "
    print *, A

    print *

    print *, "The array B contains: "
    print *, B

    print *

    C = A + 2.0*B

    print *, "C = A + 2.0 * B"
    print *, "The array C contains: "

    print *, C
end program array_arithmetic

