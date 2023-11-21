class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ## assign the arrays to A and B
        
        A,B = nums1, nums2
        ## calculate total and half
        total = len(nums1) + len(nums2)
        half = total // 2
        
        ## make sure length of A is small
        
        if len(B) < len(A):
            A, B = B, A
        
        ## the pointers
        l,r = 0, len(A) - 1
        
        ## calculate the mid for both arrays
        
        while True:
            i = (l+r) // 2
            j = half - i - 2 ## 2 because arrays are indexed at zero so one for i and i for j 
            
            ## assign values for left and right part of arrays and also check for out of bound cases
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            
            ## partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                ## for odd length
                if(total % 2):
                    return min(Aright, Bright)
                ## for even lenght
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                ## reduce the size of A
                r = i-1
                
            else:
                l = i+1
            
                        
            
            
            
            
            
            
            
        