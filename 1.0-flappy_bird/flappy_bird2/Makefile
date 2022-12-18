CXX = clang++ -std=c++17

INCLUDE = -I.

LIBS = -lsfml-graphics -lsfml-window -lsfml-system Settings.o src/*.o

main: Bird.o Settings.o main.cpp
	$(CXX) $(INCLUDE) $@.cpp -o $@ $(LIBS)

Settings.o: Settings.hpp Settings.cpp
	$(CXX) -c $(INCLUDE) Settings.cpp -o Settings.o

Bird.o: src/Bird.hpp src/Bird.cpp
	$(CXX) -c $(INCLUDE) src/Bird.cpp -o src/Bird.o

.PHONY:
clean:
	$(RM) src/*.o *.o main