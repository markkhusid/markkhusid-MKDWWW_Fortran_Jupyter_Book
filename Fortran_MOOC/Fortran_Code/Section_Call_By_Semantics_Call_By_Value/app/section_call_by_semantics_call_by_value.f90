program call_by_value
    implicit none
    integer :: n

    n = 5
    print *, n, "! = ", factorial(n)
    
    print *
    
    n = 6
    print *, n, "! = ", factorial(n)

contains

    function factorial(n) result(fac)
        implicit none
        integer, value :: n
        integer :: fac

        fac = 1
        do while (n > 1)
            fac = fac*n
            n = n - 1
        end do
    end function factorial

end program call_by_value
