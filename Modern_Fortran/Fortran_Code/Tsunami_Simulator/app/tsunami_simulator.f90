program tsunami

    implicit none
    integer :: i, n
    
    integer, parameter :: grid_size = 100
    integer, parameter :: num_time_steps = 100

    real, parameter :: dt = 1 ! time step [s]
    real, parameter :: dx = 1 ! grid spacing [m]
    real, parameter :: c  = 1 ! phase speed [m/s]

    real :: h(grid_size), dh(grid_size)
    
    integer, parameter :: icenter = 25
    real, parameter    :: decay = 0.02
    
    logical :: file_exists
    
    open(9, file = 'tsunami_simulator_data.txt')
    
    if ( grid_size <= 0 ) stop 'grid_size must be > 0'
    if ( dt <= 0 ) stop 'time step dt must be > 0'
    if ( dx <= 0 ) stop 'grid spacing dx must be > 0'
    if ( c <= 0 )  stop 'background flow speed c must be > 0'
    
    do concurrent (i = 1:grid_size)
        h(i) = exp(-decay * (i - icenter)**2)
    end do
    
    !print *, 0, h
    write (9, *) 0, h
    close(9)
    
    time_loop: do n=1,num_time_steps    
        
        dh(1) = h(1) - h(grid_size)
        
        do concurrent (i = 2:grid_size)
            dh(i) = h(i) - h(i-1)       
        end do
        
        do concurrent (i = 1:grid_size)
            h(i)=h(i)-c*dh(i) / dx * dt
        end do
        
        !print *, n, h
        inquire(file = 'tsunami_simulator_data.txt', exist = file_exists)
        if (file_exists) then
            open(9, file = 'tsunami_simulator_data.txt', status = 'old', position = 'append', action = 'write')
        else
            open(9, file = 'tsunami_simulator_data.txt', status = "new", action = 'write')
        end if
        
        write (9, *) n, h

    end do time_loop

    close (9)
    
end program tsunami
