def infinite_sequence():
    num = 2
    while True:
        yield num
        if num % 2 == 0:
            num += 2


gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
