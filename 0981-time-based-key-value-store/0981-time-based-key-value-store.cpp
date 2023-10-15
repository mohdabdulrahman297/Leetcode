#include <string>
#include <vector>
#include <map>

class TimeMap {
public:
    std::map<std::string, std::vector<std::pair<std::string, int>>> keyStore;

    TimeMap() {
        // Constructor
    }

    void set(std::string key, std::string value, int timestamp) {
        if (keyStore.find(key) == keyStore.end()) {
            keyStore[key] = std::vector<std::pair<std::string, int>>();
        }
        keyStore[key].push_back(std::make_pair(value, timestamp));
    }

    std::string get(std::string key, int timestamp) {
        std::string result = "";
        if (keyStore.find(key) != keyStore.end()) {
            std::vector<std::pair<std::string, int>>& values = keyStore[key];
            int l = 0;
            int r = values.size() - 1;
            while (l <= r) {
                int m = (l + r) / 2;
                if (values[m].second <= timestamp) {
                    result = values[m].first;
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }
        return result;
    }
};

/*
int main() {
    TimeMap time_map;

    // Set a temperature value for New York at a specific timestamp
    time_map.set("NewYork", "68°F", 100);

    // Get the temperature value for New York at a specific timestamp
    std::string result = time_map.get("NewYork", 150);

    // Print the result
    std::cout << "Result for timestamp 150: " << result << std::endl;

    return 0;
}
*/
