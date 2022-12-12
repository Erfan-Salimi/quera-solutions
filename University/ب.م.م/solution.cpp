#include<bits/stdc++.h>
using namespace std;
int main(){
long int a,b,c,s,r,d;
 
cin >> a >> b;
s = a;
for( c=b ; c>0 ; c=r ){
  r = s%c;
  s = c;
}
 
d = (a*b)/s;
cout << s;  

return 0;
}
