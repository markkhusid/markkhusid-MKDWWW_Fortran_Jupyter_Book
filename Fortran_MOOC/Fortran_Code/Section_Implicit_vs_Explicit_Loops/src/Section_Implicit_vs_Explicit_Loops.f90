module Section_Implicit_vs_Explicit_Loops
  implicit none
  private

  public :: say_hello
contains
  subroutine say_hello
    print *, "Hello, Section_Implicit_vs_Explicit_Loops!"
  end subroutine say_hello
end module Section_Implicit_vs_Explicit_Loops
