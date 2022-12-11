#include <iostream>

using namespace std;

int main()
{
    int informations[4];
    for (int i = 0; i < 4; i++) cin >> informations[i];
    if (informations[3] < informations[0]) cout << "exam did not started!" << endl;
    else if (informations[3] >= informations[1]) cout << "exam finished!" << endl;
    else{
        cout << ((informations[1] - informations[3] < informations[2]) ? informations[1] - informations[3] : informations[2]) << endl;
    }

    return 0;
}
