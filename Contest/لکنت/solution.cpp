#include <bits/stdc++.h>
using namespace std;
int main()
{
    int k = 0 , b = 1;
    char n[20];
    for(int z = 0;z < 20;z++){
    cin >> n[z];
    if(n[z] == 'L' || n[z] == 'F' || n[z] == 'T' || n[z] == 'D')k++;
    }
     
    if(k >= 1) for(int i = 0;i < k;i++) b *= 2;
      
    cout << b;
        
return 0;
}
