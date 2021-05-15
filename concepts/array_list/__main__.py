from array_list import ArrayList

numbers = ArrayList(2, 3, 5, 6, 9, 10)


for i in range(10):
    numbers.append(i)

print(" - ".join(map(lambda num: str(num), numbers)))
