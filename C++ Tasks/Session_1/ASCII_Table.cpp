#include <cctype>
#include <ios>
#include <iostream>

void ACSII_Table(void){

    std::cout << "ASCII Code Table:" << std::endl;

    for(int i = 0; i < 128; i++){
        std::cout << "ASCII Code: " << i 
        << " Hexadecimal: " << std::hex << std::uppercase << i << std::dec
        << " Character: " <<  ( (std::isprint(i) )?  static_cast<char>(i) : '.')  << std::endl;
    }
}

int main(){

    ACSII_Table();


    return 0;
}