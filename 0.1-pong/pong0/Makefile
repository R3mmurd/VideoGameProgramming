CC = clang

LIBS = -lallegro -lallegro_font -lallegro_primitives paddle.o ball.o pong.o

main: paddle.o ball.o pong.o settings.h main.c
	$(CC) main.c -o main $(LIBS)

paddle.o: paddle.h paddle.c
	$(CC) -c paddle.c

ball.o: ball.h ball.c
	$(CC) -c ball.c

pong.o: pong.h pong.c
	$(CC) -c pong.c

.PHONY:
clean:
	$(RM) *.o main