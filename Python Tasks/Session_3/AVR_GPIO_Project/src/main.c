#include <stdio.h>
             unsigned char DDRA;
             unsigned char DDRB;
             void Init_PORTA_DIR(void){
             DDRA = 0b11111110;
             printf(" The DDRA Value is: %d \n ",DDRA);
             }
             
             void Init_PORTB_DIR(void){
             DDRB = 0b11111111;
             printf(" The DDRB Value is: %d \n ",DDRB);
             }
             
             int main(){
             Init_PORTA_DIR();
             Init_PORTB_DIR();
             }
             