#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t , a , b , a1 = 0 , b1 = 0 , count = 0;
    cin >> t >> a >> b;
    while(t > 0){
    	if(count % 2 == 0){
    		t--;
    		a1++;
    		t -= a;
    		count++;
		}
		else{
			t--;
			b1++;
			t -= b;
			count++;
		}
	}
    cout << a1 << " " << b1;
    return 0;
}
