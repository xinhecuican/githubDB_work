# makefile for screened coulombic potential computation with cuda
#comp = nvcc
comp = gcc
flag = -c -O3  
bimpb.exe: main.o readin.o d_sign.o daxpy.o dcopy.o ddot.o dgemv.o dnrm2.o drot.o drotg.o dscal.o dtrsv.o gmres.o gl_functions.o treecode.o pp_timer.o
	$(comp) -o bimpb.exe *.o -lm
pp_timer.o: pp_timer.c
	$(comp) $(flag) pp_timer.c
main.o: main.c
	$(comp) $(flag) main.c
readin.o: readin.c
	$(comp) $(flag) readin.c
d_sign.o: d_sign.c
	$(comp) $(flag) d_sign.c
daxpy.o: daxpy.c
	$(comp) $(flag) daxpy.c
dcopy.o: dcopy.c
	$(comp) $(flag) dcopy.c
ddot.o: ddot.c
	$(comp) $(flag) ddot.c
dgemv.o: dgemv.c
	$(comp) $(flag) dgemv.c
dnrm2.o: dnrm2.c
	$(comp) $(flag) dnrm2.c
drot.o: drot.c
	$(comp) $(flag) drot.c
drotg.o: drotg.c
	$(comp) $(flag) drotg.c
dscal.o: dscal.c
	$(comp) $(flag) dscal.c
dtrsv.o: dtrsv.c
	$(comp) $(flag) dtrsv.c
gmres.o: gmres.c
	$(comp) $(flag) gmres.c
gl_functions.o: gl_functions.c
	$(comp) $(flag) gl_functions.c
treecode.o: treecode.c
	$(comp) $(flag) treecode.c
matvec.o: matvec.c
	$(comp) $(flag) matvec.c
clean: 
	\rm -f *.o 





