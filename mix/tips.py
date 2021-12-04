# Incorrect
def add_plush(num):
    return num + 1

print(add_plush(5))


# Correct
add_number = lambda x: x+1
print(add_number(5))

lst = ['word','word','multiple words','word']
display = [word for words in lst for word in words.split()]
print(display)
