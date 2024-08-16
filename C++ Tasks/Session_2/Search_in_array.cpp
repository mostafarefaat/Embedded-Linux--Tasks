#include <ios>
#include <iostream>


bool Search_in_array(double const arr[], int size, double num){
   
    for(int i = 1; i < size; i++){
        if(arr[i] == num){
            return true;
        }
    }
    return false;;

}

int main(){

    int size =0;
    double num = 0;
    // Define and initialize the array with some values.
    std::cout << "Please Enter The Size Of The Array" << std::endl;
    std::cin >> size;
    double arr[size];
    std::cout << "Please Enter The Elements Of The Array" << std::endl;
    for(int i =0; i<size; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr[i];
    }
    std::cout << "Please Enter The Number You Want To Find" << std::endl;
    std::cin >> num;
    std::cout << std::boolalpha << Search_in_array(arr,size,num) << std::noboolalpha << std::endl;
    return 0;
}