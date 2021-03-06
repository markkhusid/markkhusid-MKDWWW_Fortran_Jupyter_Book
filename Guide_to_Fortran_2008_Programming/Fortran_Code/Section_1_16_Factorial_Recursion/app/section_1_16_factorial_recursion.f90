module factorial_module

    implicit none
    public :: factorial

contains

    recursive function factorial(n) result (factorial_result)

        integer, intent(in) :: n
        integer :: factorial_result

        if (n <= 0) then
            factorial_result = 1
        else
            factorial_result = n * factorial(n - 1)
        end if

    end function factorial

end module factorial_module

program test_factorial
    
    use factorial_module
    implicit none

    integer :: n

    read *, n ! Will be piped in from command line
    print *
    write (unit = *, fmt = "(i10, a, i10)") n, "! = ", factorial(n)

end program test_factorial

