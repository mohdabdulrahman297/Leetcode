class MyHashSet {
public:
    bool set[1000001];
    MyHashSet() {
        for (int i = 0; i < 1000001; i++) {
            set[i] = false;
        }
    }
    
    void add(int key) {
        set[key] = true;
    }
    
    void remove(int key) {
        set[key] = false;
    }
    
    bool contains(int key) {
        return set[key];
    }
};

/*
int main() {
    MyHashSet obj;

    obj.add(1);
    obj.add(2);
    obj.add(3);

    std::cout << "Contains 2: " << obj.contains(2) << std::endl; // Output: Contains 2: 1 (true)
    std::cout << "Contains 4: " << obj.contains(4) << std::endl; // Output: Contains 4: 0 (false)

    obj.remove(2);
    
    std::cout << "Contains 2: " << obj.contains(2) << std::endl; // Output: Contains 2: 0 (false)

    return 0;
}
*/