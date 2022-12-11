#include <iostream>

using namespace std;

int main()
{
    int number, counting = 0;
    cin >> number;
    if (number % 2 == 1 && number != 1){
        for (int i = 2; i <= number / 2; i++){
            if (number % i == 0){
                counting++;
            }
            if (counting == 1) break;
        }
        cout << ((counting == 0) ? "zoj" : "fard") << endl;
    }
    else cout << "fard" << endl;

    return 0;
}
