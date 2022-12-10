#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, m;
	string b;
	cin >> m >> n;
	int a[m] = {0};

	for (int i = 0; i < n; i++){
		cin >> b;
		for (int j = 0; j < m; j++){
			if (b[j] == 'W')
				a[j] += 1;
		}
	}
    
	for (int i = 0; i < m; i++){
		if (a[i] % 2 == 0)
			cout << "B";
		else
			cout << "F";
	}
}