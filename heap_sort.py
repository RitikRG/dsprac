class Heap:
    def __init__(self):
        self.heap=[]
    def create_heap(self,arr):
        for i in arr:
            self.insert(i)
    def insert(self,e):
        index = len(self.heap)
        parentIndex = (index-1)//2

        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else: 
                self.heap[index]=self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index-1)//2
        if (index==len(self.heap)):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def display(self):
        print(self.heap)

    def delete(self):
        if len(self.heap)==0: return
        if len(self.heap)==1: return self.heap.pop()

        # saving the original root
        root = self.heap[0]

        # replacing root with last element of the heap
        self.heap[0] = self.heap[len(self.heap)-1]

        # removing the last element Duplicate 
        self.heap.pop()

        temp = Heap()
        temp.create_heap(self.heap)
        self.heap = temp.heap
        return root
    
    def heap_sort(self):
        output = []
        while len(self.heap)>0:
            output.insert(0,self.delete())
        return output

    

h = Heap()
h.create_heap([10,3,14,2,1,5,18])
h.display()

print(h.heap_sort())