program linenumbers

! declare variables

implicit none

integer             :: i, rdopst, wropst, rdst
character(30)       :: rdfile, wrfile
character(132)      :: line

! --------------------
! dsiplay initial header

print *
write (*,'(a)') "Line Number Example Program"

! --------------------
! Set rdfile to input_test_file.txt for Jupyter Notebook
rdfile = "input_test_file.txt"

open (  12, file = rdfile, status = "old",      &
        action = "read", position = "rewind",   &
        iostat = rdopst )

! Check if file exists
print * ! skip a line on screen
if (rdopst /= 0) then
    write (*, '(a,a)', advance = "no") "Unable to open input file -> ", rdfile
    stop
else
    write (*, '(a,a)', advance="no") "Opened input file for reading -> ", rdfile
end if
print * ! skip a line on screen

! --------------------
! Set wrfile to output_test_file for Jupyter Notebook

wrfile = "output_test_file.txt"

open (  14, file = wrfile, status = "replace",  &
        action = "write", position = "rewind",  &
        iostat = wropst )

print * ! skip a line on screen
if (wropst /= 0) then
    write (*, '(a,a)', advance="no") "Unable to open output file -> ", wrfile
    stop
else 
    write (*, '(a,a)', advance="no") "Opened output file for writing -> ", wrfile
end if
print * ! skip a line on screen

! --------------------
! Process input file and add line numbers.  Write result to output file
print * ! skip a line on screen
write (*, '(a)') "Processing input file and writing output file...."
print * ! skip a line on screen
i = 1
do
    ! read line from input file
    read (12, '(a)', iostat = rdst) line

    ! if end of file, exit loop
    if (rdst > 0) stop "read error"
    if (rdst < 0) exit

    write (*, '(a, a)', advance="no") "Read line from input file -> ", line

    ! write line number and line to output file
    write (14, '(i10, 2x, a)') i, line
    print * ! skip line on screen
    write (*, '(a, i10, 2x, a)', advance="no") "Wrote line to output file -> ", i, line
    print * ! skip line on sreen
    i = i + 1
        
end do

print * ! skip line on screen

! close files

close (12)
close (14)

end program linenumbers

