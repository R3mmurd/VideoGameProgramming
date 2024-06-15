CXX = clang++ -std=c++17

INCLUDE = -I.

BUILD_DIR = build

OBJ_RULES = Settings.o Game.o Bird.o Log.o LogPair.o World.o

LIBS = -lsfml-graphics -lsfml-audio -lsfml-window -lsfml-system $(BUILD_DIR)/*.o

main: $(BUILD_DIR) $(OBJ_RULES) main.cpp
	$(CXX) $(INCLUDE) $@.cpp -o $@ $(LIBS)

Settings.o: Settings.cpp Settings.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

Game.o: src/Game.cpp src/Game.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

Bird.o: src/Bird.cpp src/Bird.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@
	
Log.o: src/Log.cpp src/Log.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

LogPair.o: src/LogPair.cpp src/LogPair.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

World.o: src/World.cpp src/World.hpp
	$(CXX) -c $(INCLUDE) $< -o $(BUILD_DIR)/$@

$(BUILD_DIR):
	mkdir -p $@

.PHONY:
clean:
	$(RM) -r $(BUILD_DIR) main