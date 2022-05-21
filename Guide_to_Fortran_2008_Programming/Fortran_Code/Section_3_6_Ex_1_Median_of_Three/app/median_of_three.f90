program median_of_3_program

    implicit none

    real :: num1, num2, num3
    real :: median
    
    write (*, '(a)') "This program finds the median of three numbers....."
    write (*, '(a)') "Data piped in from command line...."
    read *, num1, num2, num3
    
    write (*, '(a, 3f10.2)') "The three entered numbers were -->", num1, num2, num3
    
    median = medianOf3(n1=num1, n2=num2, n3=num3)
    
    write (*, '(a, f10.2)') "The median value is -->", median
 
    contains

        subroutine swap(a, b)
            real, intent (in out) :: a, b
            real :: temp
            temp = a
            a = b
            b = temp
        end subroutine swap
    
        subroutine sort(val1, val2, val3)
            real, intent(in out) :: val1, val2, val3
        
            if (val1 > val2) then
                call swap (val1, val2)
            end if
            if (val1 > val3) then
                call swap (val1, val3)
            end if
            if (val2 > val3) then
                call swap (val2, val3)
            end if
        end subroutine sort

        function medianOf3(n1, n2, n3) result (median_value)
 
            real, intent(in out) :: n1, n2, n3
            real :: median_value
        
            call sort (val1=n1, val2=n2, val3=n3)
            
            median_value = n2
     
        end function medianOf3

end program median_of_3_program
