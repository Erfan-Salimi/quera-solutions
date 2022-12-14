#include <iostream>

using namespace std;

int main()
{
    int number, j = 1;
    cin >> number;
    for (int i = 0; i < 4; i++){
        cout << "########.......########" << endl;
        if (j <= number){
            cout << "#ghorfe" << j << ".......";
            j++;
            if (j <= number){
                cout << "ghorfe" << j << "#" << endl;
                j++;
            }
            else cout << ".......#" << endl;
        }
        else cout << "#.....................#" << endl;
    }
    cout << "#######################" << endl;

    return 0;
}
