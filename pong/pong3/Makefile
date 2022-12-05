CC = clang

LIBS = -lallegro -lallegro_font -lallegro_primitives -lallegro_font -lallegro_ttf fonts.o paddle.o ball.o pong.o

main: paddle.o ball.o pong.o fonts.o configuration.h main.c
	$(CC) main.c -o main $(LIBS)

fonts.o: fonts.h fonts.c
	$(CC) -c fonts.c

paddle.o: paddle.h paddle.c
	$(CC) -c paddle.c

ball.o: ball.h ball.c
	$(CC) -c ball.c

pong.o: pong.h pong.c
	$(CC) -c pong.c

.PHONY:
clean:
	$(RM) *.o main