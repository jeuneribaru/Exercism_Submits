#include "queen_attack.h" *ce programme ne fonctionne pas
attack_status_t can_attack(position_t queen_1, position_t queen_2) {
    if ((queen_1.row == queen_2.row) && (queen_1.column == queen_2.column) ) {
        return INVALID_POSITION;
    }
    int tab[8][8] = {0};
    tab[queen_1.row][queen_1.column] = 1;
    tab[queen_2.row][queen_2.column] = 2;
    printf(tab);
    for (int i = 0; i<8; ++i) {
        if (tab[queen_1.row][i] == 2) {
            return CAN_ATTACK;
        }
    for (int j = 0; j<8; ++j){
        if (tab[j][queen_1.column] == 2) {
            return CAN_ATTACK;
        }
    for (int k = queen_1.row; k < 8 - queen_1.row; ++k){
        if (tab[queen_1.row + k][queen_1.column +k] == 2) {
            return CAN_ATTACK;
        }
    }
    for (int l = queen_1.row; l>= 0; --l ) {
        if (tab[queen_1.row + l][queen_1.column +l] == 2) {
            return CAN_ATTACK;
        }
    }
    return CAN_NOT_ATTACK ;     
        }
    }
}
