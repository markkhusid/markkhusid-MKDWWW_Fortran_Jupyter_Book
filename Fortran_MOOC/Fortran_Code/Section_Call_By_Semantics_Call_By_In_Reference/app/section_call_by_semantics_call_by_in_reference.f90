program call_by_in_reference
    implicit none

    print *, "5! = ", factorial(5)
    print *, "10! = ", factorial(10)
    print *, "12! = ", factorial(12)

contains

    function factorial(arg) result(fac)
        implicit none
        integer, intent(in) :: arg
        integer :: fac, n

        n = arg
        fac = 1
        do while (n > 1)
            fac = fac*n
            n = n - 1
        end do
    end function factorial

end program call_by_in_reference
