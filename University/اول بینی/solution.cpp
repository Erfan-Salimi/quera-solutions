#include<bits/stdc++.h>
using namespace std;
int main()
{
    int num , i , counter , n , a;
    string b = "";
    cin >> a >> n;
    for(num = a + 1; num < n ;num++){
        counter = 0;
        for(i=2;i<=num/2;i++){
            if(num%i==0){
                counter++;
                break;
            }
        }
        if(counter==0 && num!= 1){
            b += (to_string(num) + ',');
        }
    }
    b.pop_back();
    cout << b;

    return 0;
}
