def average(number):
    total = sum(number)
    total = int(total)
    return total / len(number)


numbers = [1, 2, 3, 4, 5]
print(average(numbers))


def average_price(number):
    price = 0
    for num in number:
        price = price + num
    avg = price / len(number)
    return avg


print(average_price(numbers))
