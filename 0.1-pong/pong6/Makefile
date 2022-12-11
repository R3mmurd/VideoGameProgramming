CC = clang

LIBS = -lallegro -lallegro_font -lallegro_primitives -lallegro_font -lallegro_ttf -lallegro_audio -lallegro_acodec hitbox.o fonts.o sounds.o paddle.o ball.o pong.o

main: paddle.o ball.o pong.o fonts.o hitbox.o sounds.o configuration.h main.c
	$(CC) main.c -o main $(LIBS)

hitbox.o: hitbox.h hitbox.c
	$(CC) -c hitbox.c

fonts.o: fonts.h fonts.c
	$(CC) -c fonts.c

sounds.o: sounds.h sounds.c
	$(CC) -c sounds.c

paddle.o: paddle.h paddle.c
	$(CC) -c paddle.c

ball.o: ball.h ball.c
	$(CC) -c ball.c

pong.o: pong.h pong.c
	$(CC) -c pong.c

.PHONY:
clean:
	$(RM) *.o main