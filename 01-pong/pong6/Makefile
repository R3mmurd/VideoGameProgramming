CC = clang

INCLUDE = -I.

SRC_DIR = src
BUILD_DIR = build
OBJS = fonts.o paddle.o ball.o pong.o hitbox.o sounds.o

LIBS = -lallegro -lallegro_font -lallegro_primitives -lallegro_ttf -lallegro_audio -lallegro_acodec $(BUILD_DIR)/*o
main: main.c $(BUILD_DIR) $(OBJS)
	$(CC) $(INCLUDE) $< -o $@ $(LIBS)

fonts.o: $(SRC_DIR)/fonts.c $(SRC_DIR)/fonts.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

paddle.o: $(SRC_DIR)/paddle.c $(SRC_DIR)/paddle.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

ball.o: $(SRC_DIR)/ball.c $(SRC_DIR)/ball.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

pong.o: $(SRC_DIR)/pong.c $(SRC_DIR)/pong.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

hitbox.o: $(SRC_DIR)/hitbox.c $(SRC_DIR)/hitbox.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

sounds.o: $(SRC_DIR)/sounds.c $(SRC_DIR)/sounds.h
	$(CC) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

$(BUILD_DIR):
	mkdir -p $@

.PHONY:
clean:
	$(RM) -r $(BUILD_DIR) main