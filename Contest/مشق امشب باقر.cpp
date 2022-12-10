#include<bits/stdc++.h>
using namespace std ; 

int a , b , c ; 

int main(){
	cin >> a >> b >> c ; 

	if (a + b + c == 180 && a != 0 && b != 0 && c != 0){
		cout << "Yes";
	} else {
		cout << "No";
	}
}
