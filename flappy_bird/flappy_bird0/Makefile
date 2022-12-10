CXX = clang++ -std=c++17

LIBS = -lsfml-graphics -lsfml-window -lsfml-system

main: main.cpp
	$(CXX) $@.cpp -o $@ $(LIBS)

.PHONY:
clean:
	$(RM) main