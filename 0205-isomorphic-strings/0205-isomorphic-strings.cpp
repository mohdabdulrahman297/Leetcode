#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, vector<int>> mapST, mapTS;

        for (int i = 0; i < s.length(); i++) {
            char c1 = s[i];
            char c2 = t[i];

            mapST[c1].push_back(i);
            mapTS[c2].push_back(i);

            if (mapST[c1] != mapTS[c2]) {
                return false;
            }
        }
        return true;
    }
};

/*
int main() {
    Solution solution;

    string s = "egg";
    string t = "add";

    cout << solution.isIsomorphic(s, t) << endl;

    return 0;
}
*/
