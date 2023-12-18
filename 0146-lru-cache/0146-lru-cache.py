## time : o(1)
## space : o(n)
class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def add_node(self, new_node):
        temp = self.head.next
        new_node.next = temp
        new_node.prev = self.head
        self.head.next = new_node
        temp.prev = new_node

    def delete_node(self, del_node):
        del_prev = del_node.prev
        del_next = del_node.next
        del_prev.next = del_next
        del_next.prev = del_prev

    def get(self, key_):
        if key_ in self.cache:
            res_node = self.cache[key_]
            res = res_node.val
            del self.cache[key_]
            self.delete_node(res_node)
            self.add_node(res_node)
            self.cache[key_] = self.head.next
            return res
        return -1

    def put(self, key_, value):
        if key_ in self.cache:
            existing_node = self.cache[key_]
            del self.cache[key_]
            self.delete_node(existing_node)

        if len(self.cache) == self.cap:
            del_key = self.tail.prev.key
            del_node = self.tail.prev
            del self.cache[del_key]
            self.delete_node(del_node)

        new_node = self.Node(key_, value)
        self.add_node(new_node)
        self.cache[key_] = self.head.next


# Example usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
