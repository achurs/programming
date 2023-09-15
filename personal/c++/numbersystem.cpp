#include <iostream>
int main(){
    int number1 = 12; //int
    int number2 = 015; //octal
    int number3 = 0x12; //hex
    int number4 = 0b1100; //binary

    printf("%d %o %x %b \n", number1, number2, number3, number4);
    std::cout << "Integer:" << number1 << std::endl;
    std::cout << "Octal:" << number2 << std::endl;
    std::cout << "Hex:" << number3 << std::endl;
    std::cout << "Binary:" << number4 << std::endl;

    return 0;
}