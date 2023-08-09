class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        ##
        def merge(arr , L, M, R):
            ## create left and right subarrays
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            ## here after : in python its inclusive so M+1 means it will consider values before M+1 and similar with R+1
            i , j , k = L , 0 , 0
            
            while(j < len(left) and k < len(right)):
                if(left[j] <= right[k]):
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                    
                i+=1
            ## if any of the subarrays bounds out of range then we will handle them individually
            while(j < len(left)):
                nums[i] = left[j]
                j+=1
                i+=1
               
            while(k < len(right)):
                nums[i] = right[k]
                k+=1
                i+=1
        ## using merge sort & divide and conquer approach
        def MergeSort(arr, l , r):
            ## if left pointer is equal to right pointer
            if(l == r):
                return arr
            
            # divide the array into two halfs
            # m = mid
            m = (l+r)//2
            
            ## apply merge sort of the first half of array
            MergeSort(arr , l ,m)
            
            # ## apply merge sort of the first half of array
            MergeSort(arr , m+1 , r)
            
            ## merge function
            
            merge(arr , l , m ,r)
            return arr
        ## to run merge sort
        MergeSort(nums , 0 , len(nums)-1)
        return nums
            

        
# Create an instance of the Solution class
#solution = Solution()

# Example input array
#input_array = [38, 27, 43, 3, 9, 82, 10]

# Call the sortArray method to sort the input array
#sorted_array = solution.sortArray(input_array)

# Print the sorted array
#print(sorted_array)        
            
            
            
        