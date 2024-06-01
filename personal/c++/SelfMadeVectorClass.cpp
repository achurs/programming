#include <iostream>
#include <math.h>
class Vector{
    public:
        int *arr;
        int size;
        Vector(int size){
            this->size = size;
            arr = new int[size];
            for(int i = 0; i < size; i++){
                arr[i] = 0;
            }
        }
        Vector(int size, int values[]){
            this->size = size;
            arr = new int[size];
            int vallen = sizeof(values)/sizeof(values[0]);
            if(size >= vallen){
                for(int i = 0; i < vallen; i++){
                    arr[i] = values[i];
                }
            }
        }
        void set(int index, int value){
            arr[index] = value;
        }
        int get(int index){
            return arr[index];
        }
        void values(){
            for(int i = 0; i < size; i++){
                std::cout << arr[i] << std::endl;
            }
        }
        double magnitude(){
            double sum = 0;
            for(int i = 0; i < size; i++){
                sum += arr[i] * arr[i];
            }
            return sqrt(sum);
        }
};
int main(){
    int values[] = {3,4};
    Vector v(3,values);
    v.values();
    std::cout << "magnitude: " << v.magnitude();
    return 0;
}