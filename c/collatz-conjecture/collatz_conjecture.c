#include <stdio.h>
#include "collatz_conjecture.h"

int steps (int start) {
    int count = 0 ;
    while (start != 1) {
        if (start % 2 == 0) {
            start = start / 2 ;
        }
        else {
            start = (start * 3) + 1 ;
        }
        count += 1 ;
    }
    return count ;
}

int main(void) {
    int result = steps(12);
    printf("steps(12) = %d\n", result);
    return 0;
}