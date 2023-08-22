class Codec:
    
    def __init__(self):
        # hashmap for encoding
        self.encodeMap ={}
        # hashmap for decoding
        self.decodeMap ={}
        ## a base tiny url
        self.base = "http://tinyurl.com/"
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        ## first check if the longurl is already in the encodemap or not 
        if longUrl not in self.encodeMap:
            # then convert the long url into short url
            shortUrl  = self.base + str(len(self.encodeMap) + 1)
            # now encodeMap and decodeMap of current state
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
            
        return self.encodeMap[longUrl]    
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        ## here the input is already ecoded through previous steps
        
        return self.decodeMap[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))