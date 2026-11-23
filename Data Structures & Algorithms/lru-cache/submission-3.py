class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.key = {} 
        self.order = [] 

    def get(self, key: int) -> int:
        if key not in self.key: 
            return - 1

        self.order.remove(key) 
        self.order.append(key) 
        return self.key[key] 

    def put(self, key: int, value: int) -> None:
        if key in self.key: 
            self.key[key] = value 
            self.order.remove(key) 
            self.order.append(key) 
        else: 
            if len(self.key) == self.capacity: 
                lru = self.order[0] 
                self.key[key] = value 
                self.order.remove(lru)
                self.order.append(key) 
                del self.key[lru] 
            else: 
                self.key[key] = value 
                self.order.append(key) 


            
