#include <iostream>

using namespace std;

int main()
{
    int number, summary = 0;
    cin >> number;
    while (number > 0){
        summary += (number % 10);
        number /= 10;
    }
    cout << summary << endl;

    return 0;
}
