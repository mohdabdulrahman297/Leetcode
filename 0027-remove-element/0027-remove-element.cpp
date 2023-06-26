//Time complexity: O(n)
//Space complexity: O(1)
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        
        for(int i=0;i<nums.size();i++){
            if(nums[i] != val){
                swap(nums[i] , nums[count]);
                count++;
            }
        }
        return count;
    }
};

/*
int main() {
    vector<int> nums = {3, 2, 2, 3, 4, 5, 6};
    int val = 3;
    
    Solution sol;
    int newLength = sol.removeElement(nums, val);
    
    cout << "Modified list: ";
    for(int i = 0; i < newLength; i++){
        cout << nums[i] << " ";
    }
    
    cout << endl << "New length: " << newLength << endl;
    
    return 0;
}
*/