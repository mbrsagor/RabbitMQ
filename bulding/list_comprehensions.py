squares = []
print(squares)  # The `Squares` array inital value 0
for li in range(10):
    squares.append(li)
    # squares.append(li ** 2)

print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)
squares = [x ** 2 for x in range(10)]  # Line 9 and current line are same
print(squares)

combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

print("\n")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
_matrix = [[row[i] for row in matrix] for i in range(4)]
print(_matrix)
