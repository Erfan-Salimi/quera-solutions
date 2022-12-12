#include<bits/stdc++.h>
using namespace std;
int main(){
	int a , k;
	string num;
	cin >> k;
	for(int i = 1;i <= 5001;i++)num += to_string(i);
	cout << num[k-1];
return 0;
}
