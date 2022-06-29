class KVPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.root = Node(None)
        self.size = 0

        self.root.prev = self.root
        self.root.next = self.root

    def moveFront(self, node):
        if node is None:
            return None
        elif node.prev is not None and node.next is not None:
            # remove from current position
            self.isolate(node)

        # add to the beginning
        node.next = self.root.next
        node.prev = self.root

        # update so root points to this node
        self.root.next.prev = node
        self.root.next = node

        return node

    def unshift(self, data):
        # basically making a new node and moving it to the front
        node = Node(data)
        self.moveFront(node)
        self.size += 1
        return node

    def removeTail(self, node):
        # Check size
        if self.size == 0:
            return None

        removed = self.isolate(self.root.prev)   # since it's a circular doubly linked list
        self.capacity -= 1
        return removed

    @staticmethod
    def isolate(node):
        # delete connections on both sides of a node
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None

        return node

class LRUCache:
    def __init__(self, maxSize = 10):
        # Error check for maxSize
        if maxSize <= 0:
            raise Exception("Cache size must be great than 0")
        
        self.maxSize = maxSize
        self.ages = DoublyLinkedList()
        self.nodes = {}

    def get(self, key):
        node = self.nodes.get(key, None)

        # if node doesn't exist in cache return None
        if node is None:
            return None

        # Move to the front AKA updating the age
        self.ages.moveFront(node)

        # return the node value
        return node.data.value

    def set(self,key, value):
        node = self.nodes.get(key, None)

        # if key already exists in the cache, update the value
        if node is not None:
            node.data.value = value

            # Move to the front AKA updating the age
            self.ages.moveFront(node)
            return
        
        # if key not already in the cache & max size reached, we need to evict the LRU value
        if self.ages.size == self.maxSize:
            evicted = self.ages.removeTail()
            del self.nodes[evicted.data.key]

        self.nodes[key] = self.list.unshift(KVPair(key, value))
        