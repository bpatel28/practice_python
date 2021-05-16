from array_list import ArrayList

numbers = ArrayList()

for i in range(11):
    numbers.append(i)

numbers.append(11)

numbers.append(12)

print(numbers, f'length={len(numbers)}')

print(0 in numbers, 1 in numbers, 8 in numbers, 14 in numbers, 19 in numbers)

numbers.remove(11)

numbers.remove(2)

numbers.remove(0)

numbers.remove(12)

print(numbers, f'length={len(numbers)}')

print(0 in numbers, 1 in numbers, 8 in numbers, 14 in numbers, 19 in numbers)

numbers.insert(0, 0)

numbers.insert(2, 2)

numbers.insert(11, 11)

numbers.insert(12, 12)

print(numbers, f'length={len(numbers)}')

print(0 in numbers, 1 in numbers, 8 in numbers, 14 in numbers, 19 in numbers)
