#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N1,N3,N2=0;
    cin>>N1;
    N3 = N1 * 2;
    N3 /= 2;
    while(N1 > 0) {
        N2 = (N2 * 10) + (N1 % 10);
        N1 /= 10;
    }
   if(N3 == N2) cout << "YES";
   
   else cout << "NO";
   
    return 0;
}
