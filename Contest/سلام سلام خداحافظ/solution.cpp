#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	string name[n];
	for(int i = 0;i < n;i++) cin >> name[i];
	//salam
	for(int i = 1;i < n;i++){
		for(int x = i-1;x >= 0;x--){
			cout << name[i] << ":" << " salam " << name[x]<<"!" << endl;
		}
	}
	//khodafez
	for(int i = 0;i < n;i++){
		cout << name[i] << ": khodafez bacheha!" << endl;
		for(int x = i+1;x < n;x++){
			cout << name[x] << ": khodafez " << name[i] << "!" << endl;
		}
	}
	return 0;
}
