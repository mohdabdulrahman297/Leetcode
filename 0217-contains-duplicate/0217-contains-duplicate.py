##optimized approach
##time:o(1)
##space:o(n)
class Solution:
    def containsDuplicate(self, nums):
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False




# n = int(input("Enter the size of the array: "))
# nums = []
# print("Enter elements:")
# for _ in range(n):
#     nums.append(int(input()))

# solution = Solution()
# containsDup = solution.containsDuplicate(nums)

# if containsDup:
#     print("true")
# else:
#     print("false")
