#include<bits/stdc++.h>

using namespace std;

int a[] = {1, 1, 2, 6, 4, 2, 2, 4, 2, 8};
 
int javab(int n)
{
     if (n < 10)
        return a[n];
    if (((n/10) % 10) % 2 == 0)
        return (6 * javab(n/5) * a[n%10]) % 10;
    else
        return (4 * javab (n/5) * a[n%10]) % 10;
}
int main()
{
    int n ;
    cin >> n;
    cout << javab(n);
    return 0;
}
