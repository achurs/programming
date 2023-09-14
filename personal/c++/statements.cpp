#include <iostream>

int addNumbers(int a, int b){
    return a + b;
}
int main(){
    int firstnum = 12;
    int secondnum = 13;
    int sum = firstnum + secondnum;
    //working from main function
    std::cout << "Sum is:" << sum << std::endl;
    //working from addNumbers function
    std::cout << "Sum is:" << addNumbers(firstnum, secondnum) << std::endl;
    return 0;
}