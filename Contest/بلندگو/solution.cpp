#include<bits/stdc++.h>
using namespace std;
int main(){
	string a;
	cin >> a;
	for(int i = 0;i < a.size();i++){
		cout << a << endl;
		for(int z = 0;z <= i;z++){
		a[z] = a[i+1];
	}
	}
	return 0;
}
