#include <iostream>

void print_array(int const arr[], int size){
    for(int i = 0; i < size;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void Take_input_array(int *arr,int size){

    std::cout << "Please Enter The Elements Of The First Array" << std::endl;
    for(int i =0; i<size; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr[i];
    }

    std::cout << "-----------------------------------------------" << std::endl;

}

void Even_Odd_in_array(int *arr, int size, int *arr_even, int *even_size, int *arr_odd, int *odd_size){
    
    int even_index = *even_size;
    int odd_index = *odd_size;

    for(int i = 0; i<size; i++){
        if(arr[i] % 2 == 0){
            arr_even[even_index] = arr[i];
            even_index++;
        } else {
            arr_odd[odd_index] = arr[i];
            odd_index++;
        }
    }
    *even_size = even_index;
    *odd_size = odd_index;

}

int main(){

    int size = 0;
    int even_size = 0;
    int odd_size = 0;


    // Asking the user to enter the size of the arrays.
    std::cout << "Please Enter The Size Of The Array" << std::endl;
    std::cin >> size;
    int arr[size];
    int arr_even[size];
    int arr_odd[size];

    // Initializing the arrays with zero.
    for(int i = 0; i < size;i++){
        arr[i] = 0;
        arr_even[i] = 0;
        arr_odd[i] = 0;
    }

    Take_input_array(arr,size);

    Even_Odd_in_array(arr, size, arr_even, &even_size, arr_odd, &odd_size);

    std::cout << "-----------------------------------------------" << std::endl;

    std::cout << "Even Numbers: ";
    print_array(arr_even,even_size);
    std::cout << "Odd Numbers: ";

    print_array(arr_odd,odd_size);

    return 0;
}