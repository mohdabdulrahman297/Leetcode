class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort();
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True;
        
        return False
    
    
# Uncomment the code below to test the solution

# n = int(input("Enter the number of elements: "))
# nums = []
# print("Enter the elements: ")
# for i in range(n):
#     nums.append(int(input()))

# solution = Solution()
# containsDup = solution.containsDuplicate(nums)

# if containsDup:
#     print("true")
# else:
#     print("false")
    
        