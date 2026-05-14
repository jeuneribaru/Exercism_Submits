#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int n) {
    unsigned int s = 0;
    for (unsigned int i = 0; i <= n ; ++i ){
        s += i * i;
    }
    return s;
}

unsigned int square_of_sum(unsigned int n) {
    unsigned int s = 0;
    for (unsigned int i = 0; i <= n ; ++i) {
        s += i;
    }
    return s*s;
}

unsigned int difference_of_squares(unsigned int n) {
    return square_of_sum(n) - sum_of_squares(n);
}