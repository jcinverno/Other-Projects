#include <iostream>
#include <vector>
#include <ios> 
#include <limits> 
#include <algorithm>

using namespace std;

int main(){

    char dado {};
    int novo {};
    vector<int> valores {1, 2, 3};

    do {
        cout << "\nP - Print numbers \nA - Add a number \nM - Dispay mean of the numbers \nS - Display the smallest number \nL - Display the largest number \nQ - Quit \n\nEnter your choice: ";
        cin >> dado;

        char up = toupper(dado);

        switch (up){
                    case 'P':

                        if (valores.empty() == false){
                            cout << "[ ";
                            for (auto i: valores)
                                cout << i << ' ';
                            cout << "]" <<endl;
                        }
                        else
                            cout << "[] - the list is empty\n";
                       
                        break;
                        
                    case 'A':

                        while (cout << "What number do you want to add? \n " && !(cin >> novo)) {
                            cin.clear();
                            cin.ignore(numeric_limits<streamsize>::max(), '\n');
                            cout << "Invalid input; please re-enter.\n";
                        }

                        valores.push_back(novo);
                        cout << "Number " << novo << " added" <<endl;
                        break;

                    case 'M':

                        if (valores.empty() == false){
                            int tamanho = 0;
                            int soma = 0;
                            tamanho = valores.size();

                            for (auto i: valores)
                                soma += i;
                            double media = (double)soma / (double)tamanho;

                            cout << "The mean is: " << media <<endl;
                        }
                        else
                            cout << "Unable to calculate the mean - no data.\n";

                        break;

                    case 'S':
                        if (valores.empty() == false){
                            cout << "The smallest number is: " << *min_element(valores.begin(), valores.end()) <<endl;
                        }
                        else
                        cout << "Unable to determine the smallest number - list is empty.\n";
                        
                        break;

                    case 'L':
                        if (valores.empty() == false){
                            cout << "The largest number is: " << *max_element(valores.begin(), valores.end()) <<endl;
                        }
                        else
                        cout << "Unable to determine the largest number - list is empty.\n";

                        break;
                    case 'Q':
                        cout << "Goodbye!" << endl;
                        break;
                    default:
                        cout << "Sorry, invalid choice. Choose again. " << endl;
                        break;
                    }

    } while (dado != 'Q' and dado != 'q');

    return 0;

}
