#include<bits/stdc++.h>
using namespace std;

int main()
{
	int f,n,i;
	f = 1;
	cin>>n;
    	for (i = n; i > 0; i--) f *= i;
    
    cout<<f;

return 0;
}
