#include <iostream>


int main(){

    double number = 0;


    std::cout << "Please Enter A Number " << std::endl;
    std::cin >> number;

    auto fun = [number](){
        double number_squre = number*number;
        std::cout << "Square of the number is: " << number_squre << std::endl;
    };

    fun();
    
    return 0;
}