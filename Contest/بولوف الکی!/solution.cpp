#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, sum = 0;
    string a, b , c;
    cin >> n;
    for (int i = 0; i <= n; i++){
    	if(i == 0){
    		getline(cin, c);
		}
    	else{
		
        getline(cin, a);
        a.erase(remove_if(a.begin(), a.end(), ::isspace), a.end());
        
        getline(cin, b);
        b.erase(remove_if(b.begin(), b.end(), ::isspace), b.end());

         if (a != b) sum++;
     }
}
    cout << sum;

    return 0;
}
