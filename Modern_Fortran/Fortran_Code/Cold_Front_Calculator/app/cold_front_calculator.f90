program cold_front

    implicit none
    
    real :: temp1 = 12 ! degrees C
    real :: temp2 = 24 ! degrees C
    real :: dx = 960   ! km
    real :: c = 20     ! km / hr
    real :: dt = 24    ! hours
    
    real :: res        ! result in degrees C
    
    res = temp2 - c * (temp2 - temp1) / dx * dt
    
    print *, "Temperature after ", dt, &
             "hours is ", res, "degrees"
             
end program cold_front