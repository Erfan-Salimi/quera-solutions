#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, result = 0, mx2 = 0, mx = 0, index, r;
    cin >> n;
    int ls[n];

    for (int i=0; i<n; i++){
        cin >> ls[i];
    }
    mx = *max_element(ls, ls + n);

    for (int i=0; i<n; i++){
        if (ls[i] > mx2)
            mx2 = ls[i];

        index = 0;
        for (int j=0; j<n; j++){
            index = j;
            if (ls[j] == mx)
                break;
        }

        if (i > index){
            mx = 0;
            for (int j=i+1; j<n; j++){
                if (ls[j] > mx)
                    mx = ls[j];
            }
        }
        if (mx <= mx2)
            r = mx - ls[i];
        else
            r = mx2 - ls[i];
        if (r > 0)
            result += r;
    }
    cout << result;
}
