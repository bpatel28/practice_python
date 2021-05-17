from concepts.hash_table import HashTable

data = HashTable()
for i in range(0, 10):
    data.add(i, i + 100)

data.add(0, 1)

print(data, f'length={len(data)}', data._capacity)

for i in range(10, 20):
    data.add("xyz" + str(i), 'yz' + str(i))

print(data, f'length={len(data)}', data._capacity)

data.remove(1)
data.remove(3)

print(data[4])

print(data, f'length={len(data)}', data._capacity)

for k, v in data:
    print(k, v)
