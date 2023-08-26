class Solution {
    
private:
    unordered_map<string,string> encodeMap;
    unordered_map<string,string> decodeMap;
    
    string base = "http://tinyurl.com/";
    
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        
        if(encodeMap.find(longUrl) == encodeMap.end()){
            
            string shortUrl = base + to_string(encodeMap.size() + 1);
            encodeMap[longUrl] = shortUrl;
            decodeMap[shortUrl] = longUrl;
        }
        
        return encodeMap[longUrl];
        
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        
        return decodeMap[shortUrl];
        
    }
};

/*
int main()
{
Codec codec;
string url = "http://tinyurl.com/";
string encoded = codec.encode(url);
string decoded = codec.decode(encoded);

std::cout << "Original URL: " << url << std::endl;
    std::cout << "Encoded URL: " << encoded << std::endl;
    std::cout << "Decoded URL: " << decoded << std::endl;

    return 0;
}*/

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));