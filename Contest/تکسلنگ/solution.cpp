#include<bits/stdc++.h>
using namespace std;
int main(){
	string a , b , c;
	cin >> a >> b >> c;
	for(int i = 0;i < a.size();i+=5){
		if(a[i] == '*' && a[i+1] == '*' && a[i+2] == '*' && a[i+3] == '*' && a[i+4] == '*')cout << "T";
		else if(a[i] == 'o' && a[i+1] == 'o' && a[i+2] == '*' && a[i+3] == 'o' && a[i+4] == 'o')cout << "A";
		else if(a[i] == '*' && a[i+1] == 'o' && a[i+2] == 'o' && a[i+3] == 'o' && a[i+4] == '*'){
			if(b[i] == 'o' && b[i+1] == 'o' && b[i+2] == '*' && b[i+3] == 'o' && b[i+4] == 'o') cout <<"X";
			else cout << "N";
		}
		else cout << "M";
	}

	return 0;
}
