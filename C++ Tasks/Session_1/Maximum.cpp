#include <algorithm>
#include <iostream>

int main(){
    int num1;
    int num2;
    int num3;
    std::cin >> num1; 
    std::cin >> num2; 
    std::cin >> num3;

    int max = std::max({num1, num2, num3});
    int min = std::min({num1, num2, num3});

    std::cout << "The Maximum Number is: " << max << std::endl;
    std::cout << "The Minimum Number is: " << min << std::endl;

    return 0;
}