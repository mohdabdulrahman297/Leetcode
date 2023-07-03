class NumArray:

    def __init__(self, nums: List[int]):
        ## sum for an entire array
        ## create an array named prefix
        
        self.prefix = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefix[right]
        leftsum =0
        
        if(left > 0):
            leftsum = self.prefix[left-1]
            
        return rightsum - leftsum
    
    
# Example usage
#ums = [-2, 0, 3, -5, 2, -1]

# Create an instance of NumArray
#bj = NumArray(nums)

# Calculate and print the sum of a range
#eft = 0
#ight = 2
#aram_1 = obj.sumRange(left, right)
#rint(param_1)  # Output: 1

#eft = 2
#ight = 5
#aram_2 = obj.sumRange(left, right)
#rint(param_2)  # Output: -1

#eft = 0
#ight = 5
#aram_3 = obj.sumRange(left, right)
#rint(param_3)  # Output: -3
#   
                                  
                                  
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)