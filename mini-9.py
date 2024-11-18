class LRUCache:

    def __init__(capacity=16):
        storage = {}
        tickstamp = 0

    def put(self, key, value):
        if len(self.storage.keys()) < capacity:
            storage[key] = [value, tickstamp]
            tickstamp += 1
        else:
            min_key = sorted(storage.items, key = lambda x: x[1][1])[0]
            del storage[min_key]
            storage[key] = [value, tickstamp]
            tickstamp += 1
    
    def get(self, key):
        return self.storage[key]
