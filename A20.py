#Pythonn illustration of use of is in python
x = 5
if (type(x) is int):
    print("True")
else:
    print("False")
x2 = 5.5
if (type(x2) is not float):
    print("True")
else:
    print("False")
x3 = 20
y = 20
if (x3 is y):
    print("x3 and Y have the same identity")
y2 = 30
if (x3 is not y2):
    print("X3 and Y2 have different identities")