CXX = clang++ -std=c++17

INCLUDE = -I.

BUILD_DIR = build

OBJ_RULES = Settings.o Game.o Bird.o Log.o LogPair.o World.o StateMachine.o TitleScreenState.o CountDownState.o PlayingState.o

LIBS = -lsfml-graphics -lsfml-audio -lsfml-window -lsfml-system $(BUILD_DIR)/*.o

main: $(BUILD_DIR) $(OBJ_RULES) main.cpp
	$(CXX) $(INCLUDE) $@.cpp -o $@ $(LIBS)

Settings.o: $(BUILD_DIR) Settings.hpp Settings.cpp
	$(CXX) -c $(INCLUDE) Settings.cpp -o $(BUILD_DIR)/$@

Game.o: $(BUILD_DIR) src/Game.hpp src/Game.cpp
	$(CXX) -c $(INCLUDE) src/Game.cpp -o $(BUILD_DIR)/$@

Bird.o: $(BUILD_DIR) src/Bird.hpp src/Bird.cpp
	$(CXX) -c $(INCLUDE) src/Bird.cpp -o $(BUILD_DIR)/$@
	
Log.o: $(BUILD_DIR) src/Log.hpp src/Log.cpp
	$(CXX) -c $(INCLUDE) src/Log.cpp -o $(BUILD_DIR)/$@

LogPair.o: $(BUILD_DIR) src/LogPair.hpp src/LogPair.cpp
	$(CXX) -c $(INCLUDE) src/LogPair.cpp -o $(BUILD_DIR)/$@

World.o: $(BUILD_DIR) src/World.hpp src/World.cpp
	$(CXX) -c $(INCLUDE) src/World.cpp -o $(BUILD_DIR)/$@

StateMachine.o: $(BUILD_DIR) src/states/StateMachine.hpp src/states/StateMachine.cpp
	$(CXX) -c $(INCLUDE) src/states/StateMachine.cpp -o $(BUILD_DIR)/$@

TitleScreenState.o: $(BUILD_DIR) src/states/TitleScreenState.hpp src/states/TitleScreenState.cpp
	$(CXX) -c $(INCLUDE) src/states/TitleScreenState.cpp -o $(BUILD_DIR)/$@

CountDownState.o: $(BUILD_DIR) src/states/CountDownState.hpp src/states/CountDownState.cpp
	$(CXX) -c $(INCLUDE) src/states/CountDownState.cpp -o $(BUILD_DIR)/$@

PlayingState.o: $(BUILD_DIR) src/states/PlayingState.hpp src/states/PlayingState.cpp
	$(CXX) -c $(INCLUDE) src/states/PlayingState.cpp -o $(BUILD_DIR)/$@


$(BUILD_DIR):
	mkdir -p $@

.PHONY:
clean:
	$(RM) $(BUILD_DIR)/*.o main