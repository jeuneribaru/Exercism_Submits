#include "grains.h"

uint64_t square (uint8_t index) {
    if (index == 0 || index > 64) {
        return 0;
    }
    uint64_t result = 1;
    for (uint8_t i = 1; i < index; ++i) {
        result *= 2;
    }
    return result;
}

uint64_t total(void) {
    uint64_t somme = 0;
    for (uint8_t j = 1; j <= 64; ++j) {
        somme += square(j);
    }
    return somme;
}