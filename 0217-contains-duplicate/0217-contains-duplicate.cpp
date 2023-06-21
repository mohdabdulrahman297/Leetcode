//optimized approach
//time:o(1)
//space:o(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(int i=0;i<nums.size();i++){
            if(s.find(nums[i]) != s.end()){
                return true;
            }
            s.insert(nums[i]);
        }
        return false;
    }
};


/*
int main(){
    int n;
    cout<<"enter size of array"<<endl;
    cin>>n;
    
    vector<int> nums(n);
    
    cout<<"enter elements"<<endl;
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }
    
    Solution solution;
    
    bool containsDup = solution.containsDuplicate(nums);
    
    if(containsDup){
        cout<<"true"<<endl;
    }
    else{
        cout<<"false"<<endl;
    }
    return 0;
}
*/