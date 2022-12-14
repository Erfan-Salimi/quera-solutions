#include <iostream>
using namespace std;
int main()
{
int n;
cin >> n;
    
   for(int i = 1 ; i <= n ; i++){
   		for(int z = 1 ; z <= n ; z++)
       		cout << z * i << " " ;
   		cout << endl;
	}
     
return 0;
}
