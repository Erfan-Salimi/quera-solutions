#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a , b , sum1 = 0, sum2 = 0;
    string answer;
    cin >> a >> b;
    while(a != 0){
    	int c = a % b;
    	answer = to_string(c) + answer;
    	a /= b;
	}
	for(int i = 0;i < answer.size();i++){
		if(i % 2 == 0) sum1 += answer[i] - '0';
		
		else sum2 += answer[i] - '0';
	}

	if(sum1 == sum2) cout << "Yes";
	else cout << "No";
    return 0;
}
