module Section_8_7_Generic_Elemental_Procedures
  implicit none
  private

  public :: say_hello
contains
  subroutine say_hello
    print *, "Hello, Section_8_7_Generic_Elemental_Procedures!"
  end subroutine say_hello
end module Section_8_7_Generic_Elemental_Procedures
