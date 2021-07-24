from concepts.max_heap import MaxHeap
import random

heap = MaxHeap()
items = []
for i in range(0, 20, 2):
    items.append(random.randrange(0, 20, 2))
    heap.insert(items[-1])

for i in range(1, 20, 2):
    items.append(random.randrange(1, 20, 2))
    heap.insert(items[-1])

print(items)

for _ in range(20):
    print(heap.remove_max())
