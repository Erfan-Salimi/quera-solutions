#include<bits/stdc++.h>
using namespace std;
int main(){
	long int m , n , y = 0 , sum = 0;
	cin >> n >> m;
	for(int i = -10;i <= m;i++){
		for(int j = 1;j <= n;j++){
			y = i + j;
			sum += y * y * y / j / j;
		}
	}
	cout << sum;
	return 0;
}
