class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_tail(self, node):
        prev_node = self.tail.prev

        node.next = self.tail
        node.prev = prev_node

        prev_node.next = node
        self.tail.prev = node


    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_tail(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self._add_to_tail(node)

            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]


def main():
    cache = LRUCache(2)
    cache.put(1,100)
    cache.put(2,200)

    print(cache.get(1))

    cache.put(3,300)
    print(cache.get(2))
    print(cache.get(3))


main()

