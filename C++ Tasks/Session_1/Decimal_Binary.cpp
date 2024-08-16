#include <iostream>
#include <string>
#include <bitset>

std::bitset<32> Decimal_to_Binary(int Number){


    std::bitset<32> binary(Number);
    return binary;

}

unsigned long Binary_to_Decimal(std::string Number){

    std::bitset<32> binary(Number);
 
    unsigned long decimal = binary.to_ulong();

    return decimal;

}

int main(){

    int Decimal;

    std::string Binary;

    std::cout << "Enter a Binary: ";
    std::cin >> Binary;

    std::cout << "Enter a Decimal: ";
    std::cin >> Decimal;

    std::cout <<std::endl;
    
    std::cout << "Decimal: " << Binary_to_Decimal(Binary) << std::endl;
    std::cout << "32-Binary: " << Decimal_to_Binary(Decimal)  << std::endl;
    
    return 0;
}