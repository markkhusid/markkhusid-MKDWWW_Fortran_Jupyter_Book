! %module magic necessary so that jupyter fortran kernel knows that 
! the code below is to be compiled as a module and not executable code.
!%module: mod_diff 
module mod_diff

    use iso_fortran_env, only: int32, real32
    implicit none
    
    private
    public :: diff_upwind, diff_centered
    
contains

    pure function diff_upwind(x) result(dx)
        real(real32), intent(in) :: x(:)
        real(real32)             :: dx(size(x))
        integer(int32)           :: im
        
        im       = size(x)
        dx(1)    = x(1) - x(im)
        dx(2:im) = x(2:im) - x(1:im - 1)
    end function diff_upwind
    
    pure function diff_centered(x) result(dx)
        real(real32), intent(in) :: x(:)
        real(real32)             :: dx(size(x))
        integer(int32)           :: im
        
        im         = size(x)
        dx(1)      = x(2) - x(im)
        dx(im)     = x(1) - x(im - 1)
        dx(2:im-1) = x(3:im) - x(1:im-2)
    end function diff_centered
    
end module mod_diff