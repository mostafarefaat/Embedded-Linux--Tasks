#include <iostream>


void print_array(double const arr[], int size){
    for(int i = 0; i < size;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void Take_input_array(double *arr,int size){

    std::cout << "Please Enter The Elements Of The First Array" << std::endl;
    for(int i =0; i<size; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr[i];
    }

    std::cout << "-----------------------------------------------" << std::endl;

}


int main(){

    int size = 0 ;
        // Asking the user to enter the size of the arrays.
    std::cout << "Please Enter The Size Of The Array" << std::endl;
    std::cin >> size;

    double arr[size];

    Take_input_array(arr,size);

    auto sort_asscending = [&arr,size](){
        for(int i = 0; i < size-1; i++){
            for(int j = 0; j < size-i-1; j++){
                if(arr[j] > arr[j+1]){
                    std::swap(arr[j],arr[j+1]);
                }
            }
        }
    };
    auto sort_descending = [&arr,size](){
        for(int i = 0; i < size-1; i++){
            for(int j = 0; j < size-i-1; j++){
                if(arr[j] < arr[j+1]){
                    std::swap(arr[j],arr[j+1]);
                }
            }
        }
    };

    sort_descending();
    std::cout << "Array In Descending Order: ";
    print_array(arr,size);

    sort_asscending();
    std::cout << "Array In Ascending Order: ";
    print_array(arr,size);

    return 0;
}