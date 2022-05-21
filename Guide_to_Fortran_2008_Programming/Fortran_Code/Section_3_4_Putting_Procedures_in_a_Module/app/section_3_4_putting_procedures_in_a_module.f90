module sort_3_module

    implicit none
    private
    real :: n1, n2, n3

    public ::   read_the_numbers, &
                sort_the_numbers, &
                print_the_numbers

    private swap

contains

    subroutine swap(a, b)
        real, intent(in out) :: a, b
        real temp
        temp = a
        a = b
        b = temp
    end subroutine swap

    subroutine read_the_numbers()
        !print *, "Enter three numbers separated by spaces:"
        read *, n1, n2, n3
        write (*, '(a, f20.3)') "Input data n1:", n1
        write (*, '(a, f20.3)') "Input data n2:", n2
        write (*, '(a, f20.3)') "Input data n3:", n3
   end subroutine read_the_numbers

   subroutine sort_the_numbers()
        if (n1 > n2) then
            call swap(n1, n2)
        end if
        if (n1 > n3) then
            call swap(n1, n3)
        end if
        if (n2 > n3) then
            call swap(n2, n3)
        end if
    end subroutine sort_the_numbers

    subroutine print_the_numbers()
        write (*, '(a)') "The numbers, in ascending order, are:"
        write (*, '(3f20.3)') n1, n2, n3
    end subroutine print_the_numbers

end module sort_3_module

program sort_3

    use sort_3_module
    implicit none

    call read_the_numbers()
    call sort_the_numbers()
    call print_the_numbers()

end program sort_3
