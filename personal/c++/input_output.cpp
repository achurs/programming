#include <iostream>
//main function
int main(){
    //inputing single name and age
    std::cout << "Enter your name: ";
    std::string name;
    //getline is used for full names or string with spaces
    std::getline(std::cin, name);
    std::cout << "Enter your age: ";
    int age;
    std::cin >> age;
    std::cout << "Hello " << name << ", you are " << age << " years old." << std::endl;
    return 0; 
}