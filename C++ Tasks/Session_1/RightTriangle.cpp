#include <iostream>
#include <algorithm>


bool isRightAngle(int side_1, int side_2, int side_3){

    int sides[3] = {side_1, side_2, side_3};
    
    std::sort(sides, sides+3);

    std::cout<< sides[0] << " " << sides[1] << " " << sides[2] <<std::endl;

    return ( (sides[0]*sides[0] + sides[1]*sides[1]) == sides[2]*sides[2] ); //A**2 + B**2 = C**2
}

int main(){
    int side1;
    int side2;
    int side3;
    std::cin >> side1;
    std::cin >> side2;
    std::cin >> side3;
    bool res = isRightAngle(side1, side2, side3);
    if( res ){
        std::cout << "The given sides form a right angle triangle." << std::endl;
    }
    else{
        std::cout << "The given sides do not form a right angle triangle." << std::endl;
    }



    return 0;
}