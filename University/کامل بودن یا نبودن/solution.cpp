#include <bits/stdc++.h>
using namespace std;
int main()
{
 int n , sum = 0;
 cin >>n;
  
  for(int i = 1; i < n ; i++){
    if( n % i == 0 ) sum += i;
  }
 if(sum == n) cout << "YES";
 
 else  cout << "NO";
 
    return 0;
}
