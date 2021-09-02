"""
Here basic concept of list data-structure
"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('sagor'))  # IF not the list return 0

print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()  # POP by default remove last one item from the list
print(fruits)
fruits.pop(0)
print(fruits)

fruits.insert(0, "Apple Mac")
print(fruits)

fruits.remove("apple")
print(fruits)

li2 = ["Java", "python", "C++"]
fruits.extend(li2)
print(fruits)

for fruit in fruits:
    print(fruit)
