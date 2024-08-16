#include <cmath>
#include <iostream>


double Max_num_in_array(double const arr[], int size){
    double max = arr[0];

    for(int i = 1; i < size; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;;

}

int main(){
    int size =0;
    // Define and initialize the array with some values.
    std::cout << "Please Enter The Size Of The Array" << std::endl;
    std::cin >> size;
    double arr[size];
    std::cout << "Please Enter The Elements Of The Array" << std::endl;
    for(int i =0; i<size; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr[i];
    }
    std::cout << "The Max Number is: " << Max_num_in_array(arr,size) << std::endl;
    return 0;
}