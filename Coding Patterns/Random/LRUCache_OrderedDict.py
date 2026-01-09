from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key) # moving to end marking as recently used

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]


def main():
    lrucache = LRUCache(2)
    lrucache.put(1,100)
    lrucache.put(2,200)

    print(lrucache.get(1))
    lrucache.put(3,300)

    print(lrucache.get(2))







main()