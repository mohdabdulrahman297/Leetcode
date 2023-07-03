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
                                  
                                  
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)