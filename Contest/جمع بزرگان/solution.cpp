#include<bits/stdc++.h>
using namespace std;
int main(){
	int z , x , y;
	string a , c , d;
	char b;
	cin >> a >> b >> c;
	
	x = a.size();
	y = c.size();
	z = abs(x-y);

	if(b == '+'){
		if(x > y){
		for(int i = 0;i < z;i++) c = '0' + c;
	}
	else if(x < y){
		for(int i = 0;i < z;i++) a = '0' + a;
	}
	
		for(int i = 0;i < a.size();i++){
			if(a[i] == '1' && c[i] == '1')cout << 2;
			else if(a[i] == '0' && c[i] == '0')cout << 0;
			else cout << 1;
		}
	}
	else if(b == '*'){
		for(int i = 0;i < a.size();i++){
			if(a[i] == '0')c += "0";
		}
		cout << c;
	}
	return 0;
}
