## space: o(n)
## time: o(logn)
class TimeMap:

    def __init__(self):
        
        ## initialize your data strucutre
        self.keyStore = {} # key : list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        ##first check if that key already exists in the hashmap
        if key not in self.keyStore:
            ## initialize an empty list for that key and then append the inputs to it
            self.keyStore[key] = []
            
        self.keyStore[key].append([value, timestamp])    
        

    def get(self, key: str, timestamp: int) -> str:
        ## initialize an empty result string and and the list of lists for the key
        res = ""
        values = self.keyStore.get(key, [])
        ##initialize the pointers
        l, r = 0, len(values) - 1
        while(l <= r):
            m = (l+r)//2
            ## check if the values list that contains the value and timestamp is less than the input timestamp
            if(values[m][1] <= timestamp):
                ##update the res string (update the value which is at values[m][0] and timestamp at values[m][1])
                res = values[m][0]
                ## increament the pointer
                l = m+1
            else:
                r = m-1
                
        return res       
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Create an instance of the TimeMap class
#time_map = TimeMap()

# Set a temperature value for New York at a specific timestamp
#time_map.set("NewYork", "68°F", 100)

# Get the temperature value for New York at a specific timestamp
#result = time_map.get("NewYork", 150)

# Print the result
#print(f"Result for timestamp 150: {result}")
