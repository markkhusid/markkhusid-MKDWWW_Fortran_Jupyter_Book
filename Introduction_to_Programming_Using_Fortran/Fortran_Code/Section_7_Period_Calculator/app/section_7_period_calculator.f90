program period

    ! Program to calculate the period of a pendulum

    ! Declare variables
    !   real constants -> gravity, pi
    !   reals -> angle, length, alpha

    implicit none

    real                :: angle, length, pperiod, alpha
    real, parameter     :: gravity = 980.0, pi = 3.14159

    ! display initial header
        
        write (*,'(a)') "Pendulum Period Calculation Program"
        print *

    ! prompt for and read the length of the angle values
    ! for the website, we will hard code the length and angle

        !write (*,'(a)', advance="no") "Enter the Length and Angle values: "
        !read (*,*) length, angle
        length = 1 ! meters
        angle = 10 ! degrees
	    write (*, '(a, f8.2, a)') "The Length is: ", length, " meters"
	    write (*, '(a, f8.2, a)') "The Angle  is: ", angle , " degrees"

    ! convert degrees to radians
        alpha = angle * pi / 180.0

    ! calculate the period
        pperiod = 2.0 * pi * sqrt(length / gravity) * ( 1.0 + 1.0/4.0 * sin( alpha / 2.0 )**2)

    ! display the results
        print *
        write (*, '(a)') "Calculating Results......"
        write (*,'(a, f8.2, a)') "The period is: ", pperiod, " seconds."
        print *

end program period
