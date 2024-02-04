#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(){

    string alphabet {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"};
    string key {"vBHedxULsfKkrMNcnwYmpuTGAIzPqbWFhSayltiVEoRJDgXQjOCZ"};
    string secret, encrip, decrip, fazer, e{'e'}, d{'d'};
    char dado{};

    do{

        cout << "Do you want to encrypt or decrypt your message? (e/d):";
        getline(cin, fazer);

        if (fazer == e){

            cout << "Enter your secret message: ";
            getline(cin, secret);

            cout << "Encrypting message..." <<endl;

            for (char s : secret){
                auto letra = alphabet.find(s);

                if (letra <= 51 and letra >= 0){

                    encrip += key.at(letra);
                }
                else 
                    encrip += s;
            }

            cout << "Encrypted message: " << encrip << endl;
            dado = 's';
        }

        else if (fazer == d){

            cout << "Enter your secret message: ";
            getline(cin, secret);

            cout << "Decrypting message..." <<endl;

            for (char a : secret){
                auto letras = key.find(a);

                if (letras <= 51 and letras >= 0){

                    decrip += alphabet.at(letras);
                }
                else 
                    decrip += a;
            };

            cout << "Decrypted message: " << decrip << endl;
            dado = 's';
        }

        else{
            cout << "Choose e or d please.";
            dado = 'n';
        }

    }while (dado != 's');

    return 0;

}

