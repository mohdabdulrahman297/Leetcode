class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        
        flowerbed.insert(flowerbed.begin() , 0);
        flowerbed.push_back(0);
        
        for(int i=1;i<flowerbed.size()-1;i++){
            if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0){
                flowerbed[i] = 1;
                n--;
            }
            if(n<=0){
                return true;
            }
        }
        
        return false;
        
    }
};

/*
int main() {
    Solution solution;

    // Test case 1
    vector<int> flowerbed1 = {1, 0, 0, 0, 1};
    int n1 = 1;
    cout << boolalpha << solution.canPlaceFlowers(flowerbed1, n1) << endl;  // Output: true

    // Test case 2
    vector<int> flowerbed2 = {1, 0, 0, 0, 1};
    int n2 = 2;
    cout << boolalpha << solution.canPlaceFlowers(flowerbed2, n2) << endl;  // Output: false

    // Test case 3
    vector<int> flowerbed3 = {0, 0, 1, 0, 1};
    int n3 = 1;
    cout << boolalpha << solution.canPlaceFlowers(flowerbed3, n3) << endl;  // Output: true

    return 0;
}
*/