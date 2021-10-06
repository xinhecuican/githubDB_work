#
# linux
LIBS = -llapack -lblas -lm


CFLAGS = -O2
#CFLAGS  = -g
CC = gcc -c
LD = gcc


HEADERS = treeGlobal.h  treecode.h
OBJ = readin.o treeGlobal.o treecode.o

%.o: %.c $(HEADERS) Makefile
	$(CC) $(CFLAGS) -o $@ $<

coulomb: coulomb.o $(OBJ)
	$(LD) -o coulomb coulomb.o $(OBJ) $(LIBS) $(LIBSLA)

clean:
	\rm -f *.o
