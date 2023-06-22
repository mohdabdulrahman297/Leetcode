//time:o(n)
//space:o(1)

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        
        int n = arr.size();
        int max = arr[n-1];
        arr[n-1] = -1;
        
        for(int i=n-2;i>=0;i--){
            int temp = max;
            if(max < arr[i]){
                max = arr[i];
            }
            arr[i] = temp;
        }
        return arr;
        
            
    }
};

/*
int main()
{
Solution solution;
vector<int> arr = {8,5,6,7,5};
vector<int> result = solution.replaceElements(arr);

for(int i:result){
cout<<i<<endl;
}
cout<<endl;
return 0;
}
*/