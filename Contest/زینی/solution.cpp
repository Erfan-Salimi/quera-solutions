#include<bits/stdc++.h>
using namespace std;
int main(){
	int n , m , sum = 0;
	cin >> n >> m;
	int a[n][m];
	for(int i = 0;i < n;i++){
		for(int x = 0;x < m;x++) cin >> a[i][x];
	}
	
	for(int i = 1;i < n-1;i++){
		for(int x = 1;x < m-1;x++){
			if( (a[i][x] > a[i][x-1] &&a[i][x] > a[i][x+1] && a[i][x] < a[i-1][x] && a[i][x] < a[i+1][x])   ||    (a[i][x] < a[i][x-1] && a[i][x] < a[i][x+1] && a[i][x] > a[i-1][x] && a[i][x] > a[i+1][x]) )sum++;
		}
	}
	cout << sum;
	return 0;
}
