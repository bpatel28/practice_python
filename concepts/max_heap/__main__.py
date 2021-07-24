from concepts.max_heap import MaxHeap


heap = MaxHeap()

for i in range(20):
    heap.insert(i)

for _ in range(20):
    print(heap.remove_max())
