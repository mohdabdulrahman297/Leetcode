// space: o(n)
// time : o(n)
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        vector<int> output;
        
        deque<int> q;
        
        int l = 0 , r = 0;
        
        while(r < nums.size()){
            while(!q.empty() && nums[q.back()] < nums[r]){
                q.pop_back();
            }
            q.push_back(r);
            
            if(l > q.front()){
                q.pop_front();
            }
            
            if(r+1 >= k){
                output.push_back(nums[q.front()]);
                l++;
            }
            
            r++;
        }
        
        return output;
        
    }
};

/*
int main() {
    Solution solution;
    std::vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    
    std::vector<int> result = solution.maxSlidingWindow(nums, k);
    
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
*/