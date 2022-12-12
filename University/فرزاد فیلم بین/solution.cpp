#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	string a;

	for(int x = 0;x <= n;x++){
		getline(cin, a);
		for(int i = 0;i < a.size();i++){
			if(i == 0){
				a[i] = toupper(a[i]);
			}
			else if(a[i] == ' '){
				a[i+1] = toupper(a[i+1]);
				i++;
			}
			else{
				a[i] = tolower(a[i]);
			}
		}
		for(int i = 0;i < a.size();i++){
			cout << a[i];
		}
	cout << endl;
	}

	
	return 0;
}
