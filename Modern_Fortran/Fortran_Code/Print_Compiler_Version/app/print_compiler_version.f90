program print_compiler_info

    use iso_fortran_env
    implicit none
    print *, 'Compiler version: ', compiler_version()
    print *, 'Compiler options: ', compiler_options()
    
end program print_compiler_info