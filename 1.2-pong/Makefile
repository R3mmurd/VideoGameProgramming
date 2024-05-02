CC = clang

INCLUDE = -I.

BUILD_DIR = build

OBJS = paddle.o ball.o pong.o fonts.o hitbox.o sounds.o

LIBS = -lallegro -lallegro_font -lallegro_primitives -lallegro_font -lallegro_ttf -lallegro_audio -lallegro_acodec $(BUILD_DIR)/*.o

main: main.c $(BUILD_DIR) $(OBJS) 
	$(CC) $(INCLUDE) $< -o $@ $(LIBS)

hitbox.o: src/hitbox.c src/hitbox.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

fonts.o: src/fonts.c src/fonts.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

sounds.o: src/sounds.c src/sounds.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

paddle.o: src/paddle.c src/paddle.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

ball.o: src/ball.c src/ball.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

pong.o: src/pong.c src/pong.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

$(BUILD_DIR):
	mkdir -p $@

.PHONY:
clean:
	$(RM) $(BUILD_DIR)/$(OBJS) main