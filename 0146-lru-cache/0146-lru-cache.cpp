class LRUCache {
public:
    // doubly linked list class
    class node {
      public:
        int key;
        int val;
        node * next;
        node * prev;
      // contructor  
      node(int _key, int _val) {
        key = _key;
        val = _val;
      }
    };
    
    // creating a head, tail and assign dummy values (-1, -1)
    node* head = new node(-1, -1);
    node* tail = new node(-1, -1);
    
    // capacity of cache
    int cap;
    // hasmap
    unordered_map<int, node*>m;
    
    
    LRUCache(int capacity) {
        // assign
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    //add node
    void addnode(node* newnode){
        node* temp = head->next;
        newnode->next = temp;
        newnode->prev = head;
        head->next = newnode;
        temp->prev = newnode;
        
    }
    
    // delete node
    void deletenode(node* delnode){
        node* delprev = delnode->prev;
        node* delnext = delnode->next;
        delprev->next = delnext;
        delnext->prev = delprev;
    }
    
    int get(int key_) {
        // first check if the key existed in cache i,e hashmap
        if(m.find(key_) != m.end()){
            // if the key exists in the map then take node address and store in hashmap by m[key_]
            node* resnode = m[key_];
            // the value will be of the node
            int res = resnode->val;
            // once done the above step delete the address because its the old adress
            m.erase(key_);
            deletenode(resnode);
            addnode(resnode);
            // add will be right after head so m[key_] will be new address
            m[key_] = head->next;
            return res;
        }
        return -1;
    }
    
    void put(int key_, int value) {
        // first check if the key existed in cache i,e hashmap
        if(m.find(key_) != m.end()){
            // if exists get the existing address
            node* existingnode = m[key_];
            m.erase(key_);
            deletenode(existingnode);
        }
        // if th size is full delete the least recently used
        if(m.size() == cap){
            // least recently used is tails previous
            m.erase(tail->prev->key);
            deletenode(tail->prev);
        }
        // add the node
        addnode(new node(key_, value));
        m[key_] = head->next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */