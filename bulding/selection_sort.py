numbers = [77, 33, 44, 11, 88, 22, 66, 65]

for number in range(len(numbers)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = number
    for num in range(number + 1, len(numbers)):
        if numbers[min_idx] < numbers[num]:
            min_idx = num

    # Swap the found minimum element with
    # the first element
    numbers[number], numbers[min_idx] = numbers[min_idx], numbers[number]

print("Sorted array below:")
for num in range(len(numbers)):
    print(numbers[num]),
