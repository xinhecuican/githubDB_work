CC = gcc
FLAGS = -c -O2
OBJECTS = main.o readin.o treecode.o

ctreecode.exe : $(OBJECTS)
	$(CC) -o ctreecode.exe *.o -lm

main.o : main.c 
	$(CC) $(FLAGS) main.c 

readin.o : readin.c
	$(CC) $(FLAGS) readin.c

treecode.o : treecode.c
	$(CC) $(FLAGS) treecode.c

clean : 
	\rm -f *.o *~







