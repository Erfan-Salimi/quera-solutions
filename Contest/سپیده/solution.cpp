#include<bits/stdc++.h>

using namespace std;

int main(){
	int n , m , i = 1;
	cin >> n >> m;
	while(m*i < n)i++;
	cout << i;
}
