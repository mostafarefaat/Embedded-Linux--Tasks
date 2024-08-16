#include <iostream>


void MultiplicationTables(int number){ //Print from Time Table 1 -> Time Table of number

    for(int i=1; i<=number; i++){

        for(int j=1; j<=10; j++){
            std::cout << i << 'x' << j << '='  << i*j << std::endl;
        }
        std::cout << "--------------------------------------------------------------" << std::endl; //Dot line after each table to separate them.
    }

}   

void MultiplicationTable(int number){ //Print number Time Table 

    for(int i=1; i<=10; i++){
        
            std::cout << number << 'x' << i << '='  << i*number << std::endl;
    }

}   

int main(){

    // MultiplicationTables(10);

    MultiplicationTable(5);

    return 0;
}