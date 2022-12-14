#include<bits/stdc++.h>
using namespace std;
int main(){
	int A;
	double a , b , c;
	cin >> a;
	A = a;
	if(A % 2 == 0){
		b = a  * a;
		c = (a+1) * 4;
		cout << fixed << setprecision(6);
		cout << b / c;
		
	}
	else{
		a -= 1;
		cout << fixed << setprecision(6);
		cout << a / 4;
	}
return 0;	
}
