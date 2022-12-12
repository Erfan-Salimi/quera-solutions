#include<bits/stdc++.h>
using namespace std;
int main()
{
	int a,b,counter,i,j;
	cin>>a>>b;
	for(i=a ; i<=b ; i++){
		counter=0;
		for( j=2 ; j<=i/2 ; j++){
			if(i%j==0) counter++;
		}
		if(counter==0 && i != 1) cout<< i << endl;
	}

	return 0;
}
