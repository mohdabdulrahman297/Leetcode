// time: o(n+m)
//space : o(n+m)
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // Creating a map nums1Idx and mapping values to their indices
        unordered_map<int, int> nums1Idx;
        for (int i = 0; i < nums1.size(); i++) {
            nums1Idx[nums1[i]] = i;
        }

        // Create a result vector of size nums1 to store the output
        vector<int> res(nums1.size(), -1);
        
        // Create an empty stack
        stack<int> st;
        
        for (int i = 0; i < nums2.size(); i++) {
            int curr = nums2[i];
            
            // Check if stack is not empty and curr is greater than the top element of the stack
            while (!st.empty() && curr > st.top()) {
                int val = st.top();
                st.pop();
                
                // Find the index of the value through the map
                int idx = nums1Idx[val];
                
                // Store the next greater element, i.e., curr, at the index correlated to nums1
                res[idx] = curr;
            }
            
            // Check if curr (next greater element) exists in nums1 and add it to the stack
            if (nums1Idx.find(curr) != nums1Idx.end()) {
                st.push(curr);
            }
        }
        
        return res;
    }
};

/*
int main() {
    Solution solution;

    // Example 1
    vector<int> nums1 = {4, 1, 2};
    vector<int> nums2 = {1, 3, 4, 2};
    vector<int> output = solution.nextGreaterElement(nums1, nums2);
    for (int num : output) {
        cout << num << " ";
    }
    cout << endl;  // Output: -1 3 -1
*/