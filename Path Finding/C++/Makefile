TARGET = main
CC = g++
CFLAGS = -Wall -g

SRCDIR = src
SRCS = main.cpp $(wildcard $(SRCDIR)/*.cpp)

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS)

clean:
	rm -f $(TARGET)

.PHONY: clean
