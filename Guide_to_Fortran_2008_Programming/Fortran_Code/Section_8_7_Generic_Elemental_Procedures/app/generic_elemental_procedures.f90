module swap_module

    implicit none

    public          :: swap
    private         :: swap_reals, swap_integers

    interface swap
        procedure swap_reals, swap_integers
    end interface

contains

    elemental subroutine swap_reals (a, b)
        real, intent (in out)   :: a, b
        real                    :: temp
        temp = a
        a = b
        b = temp
    end subroutine swap_reals

    elemental subroutine swap_integers (a, b)
        integer, intent (in out)    :: a, b
        integer                     :: temp
        temp = a
        a = b
        b = temp
    end subroutine swap_integers

end module swap_module

program generic_elemental_procedures

    use swap_module
    implicit none
    integer, dimension (3)          :: &
        i = [1, 2, 3], &
        j = [7, 8, 9]

    real, dimension (3)             :: &
        a = [1.1, 2.2, 3.3], &
        b = [7.7, 8.8, 9.9]

    print *

    write (*, '(a, 3i5)') "[*] The array i is: ", i
    write (*, '(a, 3i5)') "[*] The array j is: ", j
    
    print *

    write (*, '(a)') "[*] Now calling swap on the integer arrays...."
    print *

    call swap(i, j)

    write (*, '(a, 3i5)') "[*] After swapping, the array i is: ", i
    write (*, '(a, 3i5)') "[*] After swapping, the array j is: ", j

    print *

    write (*, '(a, 3f5.1)') "[*] The array a is: ", a
    write (*, '(a, 3f5.1)') "[*] The array b is: ", b

    print *

    write (*, '(a)') "[*] Now calling swap on the real arrays...."
    print *

    call swap(a, b)

    write (*, '(a, 3f5.1)') "[*] After swapping, the array a is: ", a
    write (*, '(a, 3f5.1)') "[*] After swapping, the array b is: ", b

end program generic_elemental_procedures

