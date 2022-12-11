#include <bits/stdc++.h>

using namespace std;

int main()
{
    string name;
    vector<int> indexes;
    for (int i = 1; i <= 5; i++){
        cin >> name;
        if (name.find("FBI") != string::npos){
            indexes.push_back(i);
        }
    }
    if (indexes.size() == 0) cout << "HE GOT AWAY!" << endl;
    else{
        sort(indexes.begin(), indexes.end());
        for (int i: indexes){
            cout << to_string(i) << ' ';
        }
    }

    return 0;
}
