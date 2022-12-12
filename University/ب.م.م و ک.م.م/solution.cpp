#include<bits/stdc++.h>
 
using namespace std;
int main(){
long int a,b,c,s,r,d;
 
cin>>a>>b;
//b.m.m
s=a;
for(c=b;c>0;c=r){
r=s%c;
s=c;
}
 //k.m.m
d=(a*b)/s;
cout<<s<<" "<<d;  
 
return 0;
}
