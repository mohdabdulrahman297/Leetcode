//time:o(n)
//space:o(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> m;
        vector<int> result;
        
        for(int i=0;i<nums.size();i++){
            int difference = target - nums[i];
            if(m.find(difference) != m.end()){
                result.push_back(m[difference]);
                result.push_back(i);
            }
            else{
                m.insert({nums[i] , i});
            }
        }
        return result;
        
    }
};

/*
int main()
{

vector<int> nums = {2,7,5,11};
int target = 9;
Solution solution;
vector<int> result = solution.twoSum(nums,target);
for(int i: result):
cout<<i<<endl;
cout<<endl;
return 0;
}
*/