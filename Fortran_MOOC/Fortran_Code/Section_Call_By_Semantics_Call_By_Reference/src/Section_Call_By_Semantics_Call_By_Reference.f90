module Section_Call_By_Semantics_Call_By_Reference
  implicit none
  private

  public :: say_hello
contains
  subroutine say_hello
    print *, "Hello, Section_Call_By_Semantics_Call_By_Reference!"
  end subroutine say_hello
end module Section_Call_By_Semantics_Call_By_Reference
