#include <iostream>

using namespace std;

int main()
{
    int number, summary = 0;
    for (int i = 0; i < 5; i++){
        cin >> number;
        if (number >= 80) summary++;
    }
    if (summary >= 3) cout << "Mamma mia!" << endl;
    else if (summary == 1 || summary == 2) cout << "Mamma mia!!" << endl;
    else cout << "Mamma mia!!!" << endl;

    return 0;
}
