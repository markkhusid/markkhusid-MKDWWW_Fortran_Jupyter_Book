module Section_3_4_Putting_Procedures_in_a_Module
  implicit none
  private

  public :: say_hello
contains
  subroutine say_hello
    print *, "Hello, Section_3_4_Putting_Procedures_in_a_Module!"
  end subroutine say_hello
end module Section_3_4_Putting_Procedures_in_a_Module
