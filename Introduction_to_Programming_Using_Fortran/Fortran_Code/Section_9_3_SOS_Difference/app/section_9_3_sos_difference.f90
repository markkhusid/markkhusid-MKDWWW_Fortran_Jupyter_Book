program SOSdifference

    ! declare variables
    implicit none
    integer :: i, n, SumOfSqrs = 0, SqrOfSums = 0, difference

    ! display initial header

    !write (*,*) "Example Program"
    print *
    write (*,'(a)') "This program calculates the"
    write (*,'(a)') "difference between sum of squares "
    write (*,'(a)') "and square of sums"

    ! prompt for and read the n value
    !write (*,*) "Enter N value: "
    !read  (*,*) n
    ! Set n = 100 for Jupyter Notebook
    n = 100

    ! loop from 1 to n

    do i = 1, n
        ! compute sum of squares
        SumOfSqrs = SumOfSqrs + i ** 2

        ! compute square of sums
        SqrOfSums = SqrOfSums + i
    end do

    ! square the sums
    SqrOfSums = SqrOfSums ** 2

    ! compute the difference between sum of squares and square of sums  
    difference = SqrOfSums - SumOfSqrs

    ! display results
    print *
    write (*,'(a)') "Results..."
    print *
    write (*, '(a, i5, a, i10)') "The square of the sums from 1 to ", n, " is -> ", SqrOfSums
    print *
    write (*, '(a, i5, a, i10)') "The sum of the squares from 1 to ", n, " is -> ", SumOfSqrs
    print *
    write (*,'(a, i10)') "The difference between the square of the sums and sum of the squares is -> ", difference
    print *
end program SOSdifference
