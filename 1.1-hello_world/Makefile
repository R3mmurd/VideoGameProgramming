CC = clang

LIBS = -lallegro -lallegro_font

all: main

main: main.c
	$(CC) $@.c -o $@ $(LIBS)

.PHONY:
clean:
	$(RM) main
