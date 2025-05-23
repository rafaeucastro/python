from mainmodule.submodule.calculator import pow, multiply
from functools import reduce

myList = [1, 5, 3]
# immutable
myTuple = 1, 4, 3
myTuple = (1, 4, 5)
# immutable and have unique values
mySet = {2, 5}
mySet = set([2, 5, 5])
myDict = {
    'name': "Rafa",
    'age': 00,
    'profession': 'IT Analist'
}

print(f"My list values: {myList}")
print(f"My tuple values: {myTuple}")
print(f"My set values: {mySet}")
print(f"My dictionary values: {myDict}")
print(f"My age: {myDict['age']}")

# calling functions using different ways
print("2**8 = " + str(pow(2, 8)))
print(f"2**0 = {pow(base=2, exponent=0)}")
print(f"Multiplying the list items: {reduce(multiply, myList)}")
print(f"Adding all tuple values: {reduce(lambda x, y: x + y, myTuple)}")