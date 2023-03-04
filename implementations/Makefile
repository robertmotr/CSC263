FLAGS = -Wall -g -std=gnu99
FILES = heap.o tree.o

run_tests: ${FILES}
	gcc -DNDEBUG=1 ${FLAGS} -o $@ $^
	./run_tests > tests/actual.txt < input.txt
	diff tests/actual.txt tests/expected.txt

%.o : %.c
	gcc ${FLAGS} -c $<

.PHONY clean all
clean:
	rm *.o
	rm *.out