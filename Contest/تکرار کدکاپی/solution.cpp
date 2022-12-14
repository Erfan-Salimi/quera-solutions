#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    if (number % 8 == 0) cout << "6" << endl;
    else if(number % 8 == 1 || number % 8 == 5) cout << "c" << endl;
    else if(number % 8 == 2) cout << "o" << endl;
    else if(number % 8 == 3) cout << "d" << endl;
    else if(number % 8 == 4) cout << "e" << endl;
    else if(number % 8 == 6) cout << "u" << endl;
    else cout << "p" << endl;

    return 0;
}