// time: o(n+m)
//space : o(n+m)
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map<int , int> nums1Idx;
        
        for(int i=0;i<nums1.size();i++){
            nums1Idx[nums1[i]] = i;
            
        }
        
        
        vector<int> result;
        for(int i=0;i<nums1.size();i++){
            result.push_back(-1);
        }
        
        stack<int> stack;
        
        for(int i=0;i<nums2.size();i++){
            int curr = nums2[i];
            while(!stack.empty() && curr > stack.top()){
                int val = stack.top();
                stack.pop();
                int idx = nums1Idx[val];
                
                result[idx] = curr;
            }
            
            if(nums1Idx.find(curr) != nums1Idx.end()){
                stack.push(curr);
            }
        }
        return result;
    }
};