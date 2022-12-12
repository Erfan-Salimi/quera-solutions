#include<bits/stdc++.h>
using namespace std;
int main(){
    int num = 0, n , a , count = 0 , d = 0 , sum = 0;
    		  cin >> n;
    		  a = n;
    	//majmo argham
		while ( n != 0 ) {
		sum += n % 10 ;
		n = n / 10 ;
		}
	//adad aval
    for(num = a+1;d < sum;num++){
    	count = 0;
        for(int i = 2;i <= num / 2;i++){
            if(num % i == 0){
            	count++;
            	break;
			}
		}
		if(num != 1 && count == 0)d++;
            if(d == sum) cout << num;				 
    }
    return 0;
}
