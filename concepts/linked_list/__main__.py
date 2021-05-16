from concepts.linked_list import LinkedList, LinkedListNode

numbers = LinkedList()

for i in range(0, 11):
    numbers.append(i)

print(numbers)

print(len(numbers))

for i in range(0, 11):
    if i % 2 == 0:
        numbers.remove(i)

print(numbers)

print(len(numbers))

for i in range(0, len(numbers)):
    print(numbers[i], end=", ")
print()

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=", ")
print()

for num in numbers:
    print(num, end=", ")
print()
