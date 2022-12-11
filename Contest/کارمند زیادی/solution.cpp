#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, s = 0;
	string name, l;
	cin >> n;
	vector <int> r = {0};
	string names[n];

	for (int i = 0; i < n; i++) {
		cin >> names[i] >> l;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++){
			if (names[i] == names[j])
				s ++;
		}
		r.push_back(s);
		s = 0;
	}

	cout << *max_element(begin(r), end(r)) << endl;
}
