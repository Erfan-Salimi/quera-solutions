#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, result;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> temp;
    for (int i = 0; i < n; i++){
        if (count(nums, nums + n, nums[i]) == 1) temp.push_back(nums[i]);
    }
    if (temp.size() == 0) cout << 0 << endl;
    else if (temp.size() == 1) cout << temp[0] << endl;
    else{
        for (int i = 0; i < temp.size(); i++){
           if (i == 0) result = (temp[0] ^ temp[1]);
           else if (i != 1) result = (result ^ temp[i]);
        }
        cout << result << endl;
    }

    return 0;
}
