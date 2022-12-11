#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string result = "";
    for (int i = 1; i <= n; i++){
        result += to_string(i);
    }
    cout << result[n-1] << endl;

    return 0;
}
