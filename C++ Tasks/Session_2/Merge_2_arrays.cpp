#include <iostream>

void print_array(double const arr[], int size){
    for(int i = 0; i < size;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
void Merge_2_arrays(double *arr_res_ptr,double const arr_1[], int size_1, double const arr_2[], int size_2){
    
    int index = 0;

    for(int i = 0; i < size_1; i++){
        arr_res_ptr[i] = arr_1[i];
        index++;
    }


    for(int j = 0; j < size_2; j++){
        arr_res_ptr[index] = arr_2[j];
        index++;
    }
    

    
}
void Take_input_arrays(double *arr_1, int size_1,double *arr_2, int size_2){

    std::cout << "Please Enter The Elements Of The First Array" << std::endl;
    for(int i =0; i<size_1; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr_1[i];
    }
    
    std::cout << "Please Enter The Elements Of The Second Array" << std::endl;
    for(int i =0; i<size_2; i++){
        std::cout << "Please Enter Element: " << i+1 << std::endl;
        std::cin >> arr_2[i];
    }

    std::cout << "-----------------------------------------------" << std::endl;

}
int main(){

    int size_1 = 0;
    int size_2 = 0;

    // Asking the user to enter the size of the arrays.
    std::cout << "Please Enter The Size Of The 2 Arrays" << std::endl;
    std::cin >> size_1;
    std::cin >> size_2;

    double arr_1[size_1];
    double arr_2[size_2];

    // Allocate memory for the merged array.
    int size_res = size_1+size_2;
    double arr_res[size_res];

    Take_input_arrays(arr_1 , size_1, arr_2, size_2);

    Merge_2_arrays(arr_res,arr_1,size_1,arr_2,size_2);
       std::cout <<  "The Merged Array is : ";
       print_array(arr_res,size_res);
       std::cout << std::endl;
    
    return 0;
}