#include <vector>
#include <string>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        // Initialize two vectors for both the strings with 26 numbers set to 0
        std::vector<int> s1Count(26, 0);
        std::vector<int> s2Count(26, 0);

        for (int i = 0; i < s1.length(); ++i) {
            // Get the ASCII value
            s1Count[s1[i] - 'a'] += 1;
            s2Count[s2[i] - 'a'] += 1;
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (s1Count[i] == s2Count[i]) {
                matches += 1;
            } else {
                matches += 0;
            }
        }

        int l = 0;
        for (int r = s1.length(); r < s2.length(); ++r) {
            if (matches == 26) {
                return true;
            }

            // Get the index from the vectors for the right pointer
            int index = s2[r] - 'a';
            s2Count[index] += 1;

            // Check if the count for the characters are equal, if equal increment else decrement
            if (s1Count[index] == s2Count[index]) {
                matches += 1;
            } else if (s1Count[index] + 1 == s2Count[index]) {
                matches -= 1;
            }

            // Get the index from the vectors for the left pointer
            int leftIndex = s2[l] - 'a';
            s2Count[leftIndex] -= 1;

            if (s1Count[leftIndex] == s2Count[leftIndex]) {
                matches += 1;
            } else if (s1Count[leftIndex] - 1 == s2Count[leftIndex]) {
                matches -= 1;
            }

            l += 1;
        }

        return matches == 26;
    }
};

