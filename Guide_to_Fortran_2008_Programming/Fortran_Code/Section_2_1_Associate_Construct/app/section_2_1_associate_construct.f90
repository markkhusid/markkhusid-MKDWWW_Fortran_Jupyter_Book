program assoc

    implicit none
    real :: x = 3, y = 4

    associate (s => sqrt (x**2 + y**2))
        write (*, '(a)') "This program demonstrates the use of the Fortran associate construct"
        print *
        write (*,'(a)') "s is defined as s => sqrt (x**2 + y**2)"
        write (*, '(a, f5.1)') "x is now -> ", x
        write (*, '(a, f5.1)') "y is now -> ", y
        write (*, '(a, f5.1)') "s is equal to -> ", s 
        print *        
        write (*, '(a)') "Changing the value of x and y in the accociate block...."
        x = 5; y = 12
        write (*, '(a, f5.1, a, f5.1)') "x is now -> ", x, " y is now -> ", y
        write (*, '(a, f5.1)') "s is equal to -> ", s 
        print *
        write (*, '(a)') "Since x and y where changed in the associate block, s did not change"
        write (*, '(a, f5.1, a, f5.1)') "x still is -> ", x, " y still is -> ", y
        write (*, '(a, f5.1)') "s remains -> ", s
    end associate

    x = 5; y = 12
    associate (s => sqrt (x**2 + y**2))
        print *
        write (*, '(a)') "Now in a new associate block..."
        write (*,'(a)') "s is still defined as s => sqrt (x**2 + y**2)"
        write (*, '(a, f5.1)') "x is now -> ", x                           
        write (*, '(a, f5.1)') "y is now -> ", y
        write (*, '(a, f5.1)') "s is equal to -> ", s
    end associate

    associate (s => x)
        print *
        write (*, '(a)') "s is now defined as s => x"
        x = 9
        write (*, '(a, f5.1)') "x is now -> ", x
        write (*, '(a, f5.1)') "s is equal to -> ", s
    end associate

end program assoc
