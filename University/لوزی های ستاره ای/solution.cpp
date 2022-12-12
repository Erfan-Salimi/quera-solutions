#include<bits/stdc++.h>
using namespace std;
int main(){
	int n , star , space , chap;
	double M;
	cin >> n;
	M = n;
	if(n == 1) cout << "**";
	else{
		for(int i = 0;i < n;i++){
			if(i < M/2){
				star = 2*i+1;
				space = (n - (2*i+1))/2;
				for(int z = 0;z < space;z++) cout << " ";
				for(int w = 0;w < star;w++) cout << "*" ;
				for(int z = 0;z < space*2;z++) cout << " ";
				for(int w = 0;w < star;w++) cout << "*" ;
				cout << endl;
			}
			else{
			space = i - n/2;
			star = n - space*2;
				for(int z = 0;z < space;z++) cout << " ";
				for(int w = 0;w < star;w++) cout << "*" ;
				for(int z = 0;z < space*2;z++) cout << " ";
				for(int w = 0;w < star;w++) cout << "*" ;
				cout << endl;
				
			}
		}
	}
	return 0;
}
