#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    string num, temp;
    cin >> n;
    for (int i = 0; i < n; i++){
    	int a = 0;

        cin >> num;
            if(num[0] == num[7] && num[1] == num[6] && num[2] == num[5] && num[3] == num[4]) a++;
		
            if (a == 0){
                for (char c: num){
                    if (count(num.begin(), num.end(), c) >= 4){
                        a++;
                        break;
                    }
                }
            }
                
            if(a == 0){
            for (int i = 0;i < 6;i++){
                if(num[i] == num[i+1] && num[i+1] == num[i+2]){
                    a++;
                    break;
                	}
            	}
        	}
            
        
        if (a == 0) cout << "Rond Nist" << endl;
        else cout << "Ronde!" << endl;
    }

    return 0;
}
