program time_matrix_multiply

    ! Compare times of the matmul intrinsic vs DO loops

    implicit none
    integer, parameter :: n = 10
    real, dimension (n, n) :: a, b, c1, c2
    character(len=8) :: date
    real :: start_time_1, stop_time_1, start_time_2, stop_time_2
    real :: total_time_1, total_time_2
    integer :: i, j, k
    character(len=*), parameter :: form = "(t2, a, f0.10, a)"

    ! Get date to print on report

    call date_and_time(date = date)

    print *, "Timing report dated: " // date(1:4) &
        // "-" // date(5:6) // "-" // date(7:8)

    call random_seed()
    call random_number(a)
    call random_number(b)
    call cpu_time(start_time_1)
   
    ! Lines below added for effect
    ! The matrices of random values will be printed to the screen
    write (*, "(a)") "Matrix A"
    write (*, "(10f10.3)") (a(i,:), i=1,n)

    print *
    write (*, "(a)") "Matrix B"
    write (*, "(10f10.3)") (b(i,:), i=1,n)

    c1 = 0

    do k = 1, n
        do j = 1, n
            do i = 1, n
                c1(i, j) = c1(i, j) + a(i, k) * b(k, j)
            end do
        end do
    end do

    call cpu_time(stop_time_1)

    total_time_1 = stop_time_1 - start_time_1

    print *

    write (*, "(a)") "Matrix C1 is AxB using loops."
    write (*, "(10f10.3)") (c1(i,:), i=1,n)

    call cpu_time(start_time_2)
    c2 = matmul(a, b)
    call cpu_time(stop_time_2)

    total_time_2 = stop_time_2 - start_time_2

    print *

    write (*, "(a)") "Matrix C2 is AxB using matmul."
    write (*, "(10f10.3)") (c1(i,:), i=1,n)

    print *

    write (*, form) "Time of Do loop version is: ", total_time_1, " seconds."
    write (*, form) "Time of matmul version is: ", total_time_2, " seconds."

    print *

    if (any(abs(c1-c2) > 1.0e-4)) then
        write (*,  "(a)") "There are significantly different values between the matrices."
    else
        write (*,  "(a)") "The results are approximately the same."
    end if

    print *
    write (*, "(a, f10.3, a)") "The speedup ratio is: ", total_time_1/total_time_2, "x"

end program time_matrix_multiply
