#include <bits/stdc++.h>

using namespace std;

int main()
{
	string input, temp;
	cin >> input;
	vector<string> answer = {"ab", "ba"};
	while (answer[answer.size() - 1] != answer[answer.size() - 2]){
		temp = input;
		auto last = input.end();
		for (auto first = input.begin(); first != last; first++){
			last = remove(next(first), last, *first);
		}
		input.erase(last, input.end());
		int cnt = input.size();
		for (int i = 0; i < cnt; i++){
			if (count(temp.begin(), temp.end(), input[i]) > 1) input += to_string(count(temp.begin(), temp.end(), input[i]));
		}
		int inp_nums[input.size()];
		for (int i = 0; i < input.size(); i++){
			inp_nums[i] = input[i] - '0';
		}
		sort(inp_nums, inp_nums + input.size());
		cnt = input.size();
		input = "";
		for (int i = 0; i < cnt; i++){
			input += to_string(inp_nums[i]);
		}
		answer.push_back(input);
	}
	cout << answer[answer.size() - 2] << endl;

	return 0;
}
