CXX = clang++ -std=c++17

INCLUDE = -I.

BUILD_DIR = build

OBJ_RULES = Configuration.o Game.o Bird.o Pipe.o PipePair.o World.o

LIBS = -lsfml-graphics -lsfml-audio -lsfml-window -lsfml-system $(BUILD_DIR)/*.o

main: $(BUILD_DIR) $(OBJ_RULES) main.cpp
	$(CXX) $(INCLUDE) $@.cpp -o $@ $(LIBS)

Configuration.o: $(BUILD_DIR) Configuration.hpp Configuration.cpp
	$(CXX) -c $(INCLUDE) Configuration.cpp -o $(BUILD_DIR)/$@

Game.o: $(BUILD_DIR) src/Game.hpp src/Game.cpp
	$(CXX) -c $(INCLUDE) src/Game.cpp -o $(BUILD_DIR)/$@

Bird.o: $(BUILD_DIR) src/Bird.hpp src/Bird.cpp
	$(CXX) -c $(INCLUDE) src/Bird.cpp -o $(BUILD_DIR)/$@
	
Pipe.o: $(BUILD_DIR) src/Pipe.hpp src/Pipe.cpp
	$(CXX) -c $(INCLUDE) src/Pipe.cpp -o $(BUILD_DIR)/$@

PipePair.o: $(BUILD_DIR) src/PipePair.hpp src/PipePair.cpp
	$(CXX) -c $(INCLUDE) src/PipePair.cpp -o $(BUILD_DIR)/$@

World.o: $(BUILD_DIR) src/World.hpp src/World.cpp
	$(CXX) -c $(INCLUDE) src/World.cpp -o $(BUILD_DIR)/$@

$(BUILD_DIR):
	mkdir -p $@

.PHONY:
clean:
	$(RM) $(BUILD_DIR)/*.o main