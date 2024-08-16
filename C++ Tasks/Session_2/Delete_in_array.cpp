#include <ios>
#include <iostream>

void print_array(double const arr[], int size){
    for(int i = 0; i < size;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

bool delete_in_array(double arr[], int &size, double num){
   
    for(int i = 0; i < size; i++){
        if(arr[i] == num){
           
            //arr[i] = 0;
            for(int j = i ; j < size - i ; j++){
                arr[j] = arr[ j +1 ];
            }
            size -= 1;
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
    std::cout << "Please Enter The Number You Want To Delete:" << std::endl;
    std::cin >> num;
    std::cout << std::boolalpha << delete_in_array(arr,size,num) << std::noboolalpha << std::endl;
    std::cout << "After Deletion: " << std::endl;  // Prints the array after deletion
    std::cout << size << std::endl;
    print_array(arr,size);

    return 0;
}