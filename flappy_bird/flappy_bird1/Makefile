CXX = clang++ -std=c++17

INCLUDE = -I.

LIBS = -lsfml-graphics -lsfml-window -lsfml-system Configuration.o src/*.o

main: Bird.o Configuration.o main.cpp
	$(CXX) $(INCLUDE) $@.cpp -o $@ $(LIBS)

Configuration.o: Configuration.hpp Configuration.cpp
	$(CXX) -c $(INCLUDE) Configuration.cpp -o Configuration.o

Bird.o: src/Bird.hpp src/Bird.cpp
	$(CXX) -c $(INCLUDE) src/Bird.cpp -o src/Bird.o

.PHONY:
clean:
	$(RM) src/*.o *.o main