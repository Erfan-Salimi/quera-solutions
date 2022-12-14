#include<bits/stdc++.h>

using namespace std;

int main(){
	int n , m;
	cin >> n >> m;
	string a;
	int num[n];
	cin >> a;
	for(int i = 0;i < m;i++){
		a = a[n-1] + a;
		a.pop_back();
		for(int i = 0;i < n;i++){
			num[i] = int(a[i])+1;
			if(num[i] == 123) num[i] = 97;
			a[i] = char(num[i]);
		}
	}
	for(int i = 0;i < n;i++) cout << a[i];
	return 0;
}
