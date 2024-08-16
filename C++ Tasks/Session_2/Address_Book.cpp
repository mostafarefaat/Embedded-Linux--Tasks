#include <cctype>
#include <iomanip>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>
#include <stdlib.h>


typedef std::string string;


string input_str = "";
int input = 0;
const int size = 100;
string data;
std::vector<string> address_vect(size);

void print(std::vector<string> address_vect){

    for(int i = 0; i < address_vect.size();i++){
        std::cout << address_vect[i] << " ";
    }
    std::cout << std::endl;
}

int Search(std::vector<string> address_vect,string address){
   
    for(int i = 1; i < address_vect.size(); i++){
        if(address_vect[i] == address){
            return i;
        }
    }
    return -1;;
}

void Screen(){
    // Display the welcome message and menu options
    std::cout << "Welcome to your favorite address book!" << std::endl;
    std::cout << "What do you want to do?" << std::endl;
    std::cout << "-----------------------------------------" << std::endl;
    std::cout << std::setw(15) << "| 1. List" << std::setw(25) <<  "| List all users" <<std::endl;
    std::cout << std::setw(15) << "| 2. Add " << std::setw(25) << "| Add a new user" << std::endl;
    std::cout << std::setw(17)<<  "| 3. Delete" << std::setw(22) << "| Delete a user" << std::endl;
    std::cout << std::setw(21)<<  "| 4. Delete all" << std::setw(22) << "| Removes all users" << std::endl;
    std::cout << std::setw(17) << "| 5. Search" << std::setw(26) << "| Search for a user" << std::endl;
    std::cout << std::setw(17) << "| 6. Update" << std::setw(36) << "| Update a user's information" << std::endl;
    std::cout << std::setw(16) << "| 7. Clear" << std::setw(23) << "| Clear Console" << std::endl;
    std::cout << std::setw(15)<<  "| 8. Exit" << std::setw(36) << "| Exit the program and exit" << std::endl;
    std::cout << "-----------------------------------------" << std::endl;
}

void Add(){
        std::cout << "Enter user Name: ";
        std::cin >> data;         
        address_vect.push_back(data);
        std::cout << "User added successfully" << std::endl;
}

void Delete(){
    if(!address_vect.empty()){
        std::cout << "Enter user Name to delete: ";
        std::cin >> data;
        int index = Search(address_vect, data);
        if(index!= -1){
            address_vect.erase(address_vect.begin() + index);
            std::cout << "User deleted successfully." << std::endl;
        }else{
            std::cout << "User not found." << std::endl;
        }
    }
}

void Delete_all(){
    if(!address_vect.empty()){
        address_vect.clear();
        std::cout << "All users deleted successfully." << std::endl;
    }
}
void Search_user(){
    std::cout << "Enter user Name to search: ";
    std::cin >> data;
    int index = Search(address_vect, data);
    if(index!= -1){
        std::cout << "User found at index: " << index << std::endl;
    } else{
        std::cout << "User not found." << std::endl;
    }
}
void Update(){
    std::cout << "Enter user Name to update: ";
    std::cin >> data;
    int index = Search(address_vect, data);
    if(index!= -1){
        std::cout << "Enter new user Name: ";
        std::cin >> data;
        address_vect[index] = data;
        std::cout << "User updated successfully." << std::endl;
    } else{
        std::cout << "User not found." << std::endl;
    }
}

void Exit(){
    std::cout << "Exiting the program..." << std::endl;
    exit(0);
}
void Operation(){
    int index = 0;
    
    std::cin >> input_str;

    // Validate input
    if( std::isalpha(input_str[0]) ){
        std::cout << "Invalid choice. Please enter a number." << std::endl;
        return;
    }

    input = input_str[0] - '0';

    switch (input) {
        case 1:
            // List users
            std::cout << "List users" << std::endl;
            print(address_vect);
            break;
        case 2:
            // Add user
            Add();
            break;
        case 3:
            // Delete user
            Delete();          
            break;
        case 4:
            // Delete all users
            Delete_all();
            break;
        case 5:
            // Search user
            Search_user();
            break;
        case 6:
            // Update user
            Update();
            break;
        case 7:
            // Clear console
            system("clear");
            break;  // Clears the console screen.
        case 8: case 0 :
            // Exit
            Exit();
            break;
        default:
            std::cout << "Invalid choice. Please try again." << std::endl;
            break;
    }
}

int main(){

    for(int i=0; i<100; i++){
        address_vect[i] = "";  // initialize the array with empty strings
    }
    
do{
    Screen();

    Operation();
    
    std::cout << "-----------------------------------------" << std::endl;
    
}while (input != 0);

    return 0;
}