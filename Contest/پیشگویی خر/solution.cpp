#include<bits/stdc++.h>
using namespace std;
int main(){
	int n , m;
	cin >> n >> m;
	string a[n] , b[n];
	for(int i = 0;i < n;i++)cin >> a[i] >> b[i];
	string x;
	int y = 0;
	for(int i = 0;i < m;i++){
		cin >> x;
		for(int i = 0;i < n;i++){
			if(x == a[i]){
				y++;
				cout << b[i] << " kachal! ";
				break;
			}
		}
		if(y == 0)cout << "kachal! ";
		y = 0;
	}
	return 0;
}
