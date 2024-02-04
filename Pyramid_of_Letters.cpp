#include <iostream>
#include <string>

using namespace std;

int main(){

    //Define variables
    string pyramid, letra;

    //Ask for variable
    cout << "Enter the string you want to see in the pyramid: ";
    getline(cin, pyramid);

    //get length 
    int l = pyramid.length();

    //lines of letters
    for (int line = 0; line < l; line++) {

        letra.clear(); //clears the letters stored from the previous loop
        
        //get values from 0 to lenght
        for (int pos = 0; pos < line; pos++) {

            letra += pyramid.at(pos);

        }

        //get values from lenght to 0
        for (int posi = line; posi >= 0; posi -= 1){

            letra += pyramid.at(posi);

        }

        //prints lines of letters
        cout << letra <<endl;
    }
    return 0;
}

