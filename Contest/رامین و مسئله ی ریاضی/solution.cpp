#include <bits/stdc++.h>

using namespace std;

int main()
{
    int number, start, stop, result, first, second;
    cin >> number;
    for (int i = 0; i < number; i++){
        result = 0;
        cin >> start >> stop;
        first = sqrt(start);
        second = sqrt(stop);
        if (sqrt(start) == first){
            result++;
        }
        result += (second - first);
        cout << result << endl;
    }

    return 0;
}
