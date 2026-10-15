class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = [0]
        
        for num in nums: 
            self.add(num) 

    def add(self, val: int) -> int:
        self.heap.append(val) 
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp 
            i = i//2 
        
        while len(self.heap) - 1 > self.k: 
            self.heap[1] = self.heap[-1] 
            self.heap.pop() 

            i = 1
            n = len(self.heap) - 1
            while 2 * i <= n: 
                left = 2 * i
                right = 2 * i + 1
                smallest = left 

                if right <= n and self.heap[right] < self.heap[left]:
                    smallest = right
                if self.heap[i] <= self.heap[smallest]:
                    break

                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

                i = smallest

        return self.heap[1] 