#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, n;
	cin >> t;

	for (int i = 0; i < t; i++){
		cin >> n;
		string s;
		cin >> s;

		if (n == 1){
			string r = to_string(s[0]), result;
			int count = 1;
			for (int j = 1; j <= s.size(); j++){
				if (to_string(s[j]) == r){
					count ++;
				} else {
					result += s[j-1];
					if (count > 1)
						result += to_string(count);
					r = to_string(s[j]);
					count = 1;
				}
			}
            
			cout << result << endl;
		} else {
			string result;

			for (int j = 0; j < s.size() - 1; j++){
				if (isdigit(s[j]) == false && isdigit(s[j+1]) == true){
					string ncount;
					for (int k = j + 1; k <= s.size(); k++){
						if (isdigit(s[k]) == true)
							ncount += s[k];
						else
							break;
					}
					int number = stoi(ncount);
					for (int k = 0; k < number; k++){
						result += s[j];
					}
				} else if (isdigit(s[j]) == false && isdigit(s[j+1]) == false)
					result += s[j];
			}
			if (isdigit(s[s.size() - 1]) == false)
				result += s[s.size() - 1];

			cout << result << endl;
		}
	}
}