#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a , b , c ;
    cin >> a >> b >> c ;

        if(a * a == b * b + c * c) cout << "YES";
        
        else if(b * b == a * a + c * c) cout << "YES";
        
        else if(c * c == b * b + a * a) cout << "YES";
        
        else  cout << "NO";
        
    return 0;
}
