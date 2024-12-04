class LRUCache:
    def __init__(self, capacity=16):
        self.storage = {}
        self.capacity = capacity
        self.tickstamp = 0
    def put(self, key, value):
        if key in self.storage:
            self.storage[key] = [value, self.tickstamp]
        else:
            if len(self.storage.keys()) >= self.capacity:
                min_key = sorted(self.storage.items(), key=lambda x: x[1][1])[0][0]
                del self.storage[min_key]
            self.storage[key] = [value, self.tickstamp]
        self.tickstamp += 1
    def get(self, key):
        if key in self.storage:
            value = self.storage[key][0]
            self.storage[key][1] = self.tickstamp
            self.tickstamp += 1
            return value
        else:
            return None


cache = LRUCache(2)

cache.put(1, 'A')
cache.put(2, 'B')
print(cache.get(1))  
print(cache.get(2))  

cache.put(3, 'C')  
print(cache.get(1))  
print(cache.get(2))  
print(cache.get(3))  

cache.put(1, 'A')  
cache.put(2, 'B')  
cache.put(1, 'C')  
print(cache.get(1))  
print(cache.get(2))  

cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')  
cache.put(4, 'D')  
print(cache.get(3))  
print(cache.get(4))  
print(cache.get(1))  
print(cache.get(2))  
