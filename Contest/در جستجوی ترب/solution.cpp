#include<bits/stdc++.h>
using namespace std;
int main(){
	int x1 , v1 , x2 , v2;
	cin >> x1 >> v1 >> x2 >> v2;
	if(v1 == v2)cout << "WAIT WAIT";
	else if(v1 > v2 && x1 > x2)cout << "BORO BORO";
	else if(v2 > v1 && x2 > x1)cout << "BORO BORO";
	else cout << "SEE YOU";
	return 0;
}
