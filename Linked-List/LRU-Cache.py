import threading

class DoublyLinkedList:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # using dummy nodes for head & tail
        # to avoid edge cases when checking the head & tail with null values
        # the real head is head.next
        # the real tail is tail.prev
        self.head = DoublyLinkedList(0, 0) 
        self.tail = DoublyLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = dict()
        self.lock = threading.Lock() # to serialize access to our resources (e.g., dictionary & doubly-linked-list)

    def get(self, key: int) -> int:
        with self.lock:
            if key not in self.key_to_node:
                return -1        
            node = self.key_to_node[key]
            node = self.delete(node)
            self.addToHead(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        with self.lock:
            if key in self.key_to_node:
                node = self.key_to_node[key]
                node.value = value            
                node = self.delete(node)
                self.addToHead(node)
            else:
                node = DoublyLinkedList(key, value)
                self.key_to_node[key] = node
                self.addToHead(node)            
                if len(self.key_to_node) > self.capacity:
                    node = self.deleteLast()
                    self.key_to_node.pop(node.key)

    def delete(self, node: DoublyLinkedList) -> DoublyLinkedList:        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node
    
    def addToHead(self, node: DoublyLinkedList):
        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head
        
    def deleteLast(self) -> DoublyLinkedList:
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        return self.delete(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
