#include<iostream>

using namespace std;

int main(){
    int a, b, c, d, i, t;
    cin >> t;
    string result[t];

    for (i=0; i<t; i++){
        cin >> a; cin >> b; cin >> c; cin >> d;
        if (a+c > b+d)
            result[i] = "perspolis";
        else if (a+c < b+d)
            result[i] = "esteghlal";
        else{
            if (a > d)
                result[i] = "esteghlal";
            else if (a < d)
                result[i] = "perspolis";
            else
                result[i] = "penalty";
        }
    }
    for (i=0; i<t; i++)
        cout << result[i] << endl;

    return 0;
}
