#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, x, y, s = 0;
	cin >> n >> x >> y;
	int w[n];

	for (int i = 0; i < n; i++){
		cin >> w[i];
	}
    
	sort(w, w + n);

	for (int i = 1; i < n; i++){
		s += 100 - w[i];
    }

	int a = *min_element(w, w + n) / x;
	if (a * y >= s)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}
