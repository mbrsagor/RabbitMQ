# Incorrect
def add_plush(num):
    return num + 1

print(add_plush(5))


# Correct
add_number = lambda x: x+1
print(add_number(5))


a = 2
b = 330
print("A") if a > b else print("B")

lst = ['word','word','multiple words','word']
display = [word for words in lst for word in words.split()]
print(display)


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))
