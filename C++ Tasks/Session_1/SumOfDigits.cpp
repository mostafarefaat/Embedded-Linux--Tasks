#include <iostream>
#include <string>

int SumofDigits(int Number){

    std::string string = " ";
    int sum = 0;

    string = std::to_string(Number);

    for(char c : string){
        sum += c - '0';
    }

    return sum; 
}

int main(){

    int Number;
    std::cin >> Number ;
    std::cout << "Sum of digits: " << SumofDigits(Number) << std::endl;

    return 0;
    
}