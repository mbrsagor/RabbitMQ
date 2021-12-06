"""
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
"""



class Rectangle(object):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * self.length + 2 * self.width

class RectangleV2(Rectangle):
  pass

v2 = RectangleV2(20, 50)
print(v2.perimeter())


class Square:
  def __init__(self, length):
    self.length = length

  def area(self):
    return self.length * self.length

  def perimeter(self):
    return 4 * self.length


square = Square(4)
print(square.area())
rectangle = Rectangle(2,4)
print(rectangle.area())


class Person(object):

  
  def display():
    print("I'm calling from property method")


Person.display()

countryCode = {
  "code1": "Bangladesh",
  "code2": "India",
  "code3": "Japan"
}


def find_country(code):
  return countryCode[code]

name = find_country('code1')
print(name)
