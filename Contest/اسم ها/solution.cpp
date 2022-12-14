#include<bits/stdc++.h>
using namespace std;
int main(){
	int n = 0, k , m = 0;
	cin >> k;
	int c[k] = {0} ;
	string name;
	for(int x = 0;x < k;x++){
		cin >> name;
		for(int i = 0;i < name.size();i++){	
				for(int z = 0;z < i;z++) 
						if(name[i]!=name[z]) n++;
				if(n == i) c[x]++;
				n = 0;
		}	
	}
	m = c[0];
	for(int i = 1;i < k;i++)
			if(m < c[i]) m = c[i];
	cout << m;
	return 0;
}
