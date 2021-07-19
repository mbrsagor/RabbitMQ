x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

fruits = ("apple", "banana", "cherry")
print(fruits)
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)
