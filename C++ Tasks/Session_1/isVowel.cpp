#include <iostream>
#include <cctype>

bool isVowel(char letter){

    letter  = std::tolower(letter);
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'){
        return true;
    }
     return false;
}

int main(){

    char letter = ' ';
    std::cout << "Enter a letter: ";
    std::cin >> letter;

    if(std::isalpha(letter)){
     if(isVowel(letter)){
        std::cout << "This is a Vowel Letter" << std::endl;  
     }
     else{
        std::cout << "This is not a Vowel Letter" << std::endl;  
     }
    }
    else{
        std::cout << "Input is not a letter" << std::endl;   
        }
    return 0;
    }



