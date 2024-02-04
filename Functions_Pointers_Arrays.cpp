#include <iostream>
using namespace std;

int main(){

    const size_t array1_size {5};
    const size_t array2_size {3};

    int array1 [] {1,2,3,4,5};
    int array2 [] {10, 20, 30};

    void print (int* array, size_t size);
    int* apply_all(int* array1, size_t array1_size, int* array2, size_t array2_size);

    cout << "Array 1: " ;
    print(array1, array1_size);

    cout << "Array 2: " ;
    print(array2, array2_size);

    int *results = apply_all(array1, array1_size, array2, array2_size);
    constexpr size_t results_size {array1_size * array2_size};

    cout << "Result: ";
    print(results, results_size);

    cout << endl;

    return 0;

}

void print (int* array, size_t size){
    cout << "[ ";
    for (int i = 0; i<size; i++)
        cout << array[i] << " ";
    cout << "]" << endl;
}

int* apply_all(int* array1, size_t array1_size, int* array2, size_t array2_size){

    int count {0};
    
    int *array_ptr {nullptr};
    array_ptr = new int [array1_size * array2_size];
    for (int i = 0; i < array2_size; ++i){
    for (int l = 0; l < array1_size; ++l){
        array_ptr[count] = array1[l] * array2[i];
        ++count;
    }}
    delete [] array_ptr;
    return array_ptr; 

    }
