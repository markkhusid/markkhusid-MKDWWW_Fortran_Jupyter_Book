program main
    use, intrinsic :: iso_fortran_env, only : error_unit, DP => REAL64
    use :: linalg_mod, only : read_array, write_array
    implicit none
    ! Made info an integer because the LAPACK routine DGESV uses an explicit
    ! interface.  In the explicit interface, the argument info is an integer.
    integer :: nr_eqns, status, info
    character(len=1024) :: matrix_file_name, vector_file_name
    ! The following line no longer works because the LAPACK routine DGESV uses
    ! an explicit interface.  In the explicit interface, the argument info
    ! is an integer, but in the implicit interface, it is a character(len=1024).
    !character(len=1024) :: matrix_file_name, vector_file_name, info
    real(kind=DP), dimension(:), allocatable :: b
    integer, dimension(:), allocatable :: pivot
    real(kind=DP), dimension(:, :), allocatable :: A
    !external :: dgesv ! not needed in gfortran and throws an error

    ! Explicit interface for the LAPACK routine DGESV
    interface
        subroutine dgesv(n, nrhs, a, lda, ipiv, b, ldb, info)
            import :: DP
            implicit none
            ! .. Scalar Arguments ..
            integer, intent (Out)             :: info
            integer, intent (In)              :: lda, ldb, n, nrhs
            ! .. Array Arguments ..
            real (Kind=dp), intent (Inout)    :: a(lda, *), b(ldb, *)
            integer, Intent (Out)             :: ipiv(n)
        end subroutine dgesv
    end interface

    call get_arguments(nr_eqns, matrix_file_name, vector_file_name)

    allocate (A(nr_eqns, nr_eqns), stat=status)

    if (status /= 0) then
        write (unit=error_unit, fmt='(A)') '#error: can not allocate A'
        stop 15
    end if

    call read_array(matrix_file_name, A, [ nr_eqns, nr_eqns ])

    allocate (b(nr_eqns), stat=status)

    if (status /= 0) then
        write (unit=error_unit, fmt='(A)') '#error: can not allocate b'
        stop 15
    end if

    call read_array(vector_file_name, b, [ nr_eqns ])

    allocate (pivot(size(b)), stat=status)

    if (status /= 0) then
        write (unit=error_unit, fmt='(A, I0)') '# error: can not allocate pivot of size ', size(b)
        stop 12
    end if

    call dgesv(size(A, 2), 1, A, size(A, 1), pivot, b, size(b), info)
    
    call write_array(b)

    deallocate (A, b, pivot)

contains

   subroutine get_arguments(nr_eqns, matrix_file_name, vector_file_name)
        implicit none
        integer, intent(out) :: nr_eqns
        character(len=*), intent(out) :: matrix_file_name, vector_file_name
        integer :: status
        character(len=1024) :: buffer, msg
        
        if (command_argument_count() /= 3) then
            write (unit=error_unit, fmt='(A)') &
                '# error: argument nr_eqns, matrix_file_name, vector_file_name'
            stop 10
        end if

        call get_command_argument(1, buffer)
        read (buffer, fmt=*, iostat=status, iomsg=msg) nr_eqns
        if (status /= 0) then
            write (unit=error_unit, fmt='(2A)') '# error: ', trim(msg)
            stop 11
        end if

        call get_command_argument(2, matrix_file_name)
        call get_command_argument(3, vector_file_name)
    end subroutine get_arguments

end program main
