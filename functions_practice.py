x = 100

def thisFunction():
    age = input("Enter your age:")
    name = input("Enter your name:")
    print(name + " is " + age + " years old.")

def optionalFunction(x=1, y=2, z=3):
    print(x * y * z)

def testGlobal():
    global x
    x += 1
    print(x)



#thisFunction()
#optionalFunction(2,5)


testGlobal()
testGlobal()
testGlobal()
