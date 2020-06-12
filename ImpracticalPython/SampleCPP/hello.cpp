//============================================================================
// Name        : hello.cpp
// Author      : Ebenezer O.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <new>
using namespace std;

constexpr size_t count = 1024;	// Use for allocating space with "new"

int main() {

	printf("Allocate space for %lu long int at *ip with new\n", count);

	// allocate array
	long int * ip;

	try {
		ip = new long int [count];
	} catch (std::bad_alloc & ba) {
		fprintf(stderr, "Cannot allocate memory (%s)\n", ba.what());
		return 1;
	}

	// initialise array
	for (long int i = 0; i < count; ++i) {
		ip[i] = i;
	}
	// print array
	for (long int i = 0; i < count; ++i) {
		printf("%ld ", ip[i]);
	}
	puts("");

	// deallocate array
	delete [] ip;
	puts("space at *ip deleted");

	return 0;
}
