#include <iostream>
int main(){
    int a = 12;
    int b{13};
    std::cout << b << std::endl;
    std::cout << a << std::endl;

    std::cout << "size of b and a:"<< sizeof(b) << "," << sizeof(a) << std::endl;

    return 0;
}