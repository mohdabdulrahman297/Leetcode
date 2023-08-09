class Solution {
public:
    void Merge(vector<int> & arr, int L, int M , int R){
        vector<int> left(arr.begin() + L , arr.begin() + M+1);
        vector<int> right(arr.begin() + M+1 , arr.begin() + R+1);
            
        int i = L;
        int j =0 ;
        int k =0;
        
        while(j<left.size() && k<right.size()){
            if(left[j] <= right[k]){
                arr[i] = left[j];
                j++;
            }
            else{
                arr[i] = right[k];
                k++;
            }
            i++;
        }
        
        while(j<left.size()){
            arr[i] = left[j];
            j++;
            i++;
        }
        while(j<right.size()){
            arr[i] = right[k];
            k++;
            i++;
        }
    }
    void MergeSort(vector<int>& arr , int l , int r){
        if(l == r){
            return;
        }
        
        int m = (l+r)/2;
        
        MergeSort(arr , l , m);
        MergeSort(arr , m+1 , r);
        
        Merge(arr, l , m , r);
    }
    vector<int> sortArray(vector<int>& nums) {
        MergeSort(nums , 0 , nums.size()-1);
        return nums;
        
    }
};

/*
int main() {
    Solution solution;

    std::vector<int> input_array = {38, 27, 43, 3, 9, 82, 10};
    std::vector<int> sorted_array = solution.sortArray(input_array);

    for (int num : sorted_array) {
        std::cout << num << " ";
    }

    return 0;
}
*/