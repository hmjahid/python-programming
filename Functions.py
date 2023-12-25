def show():
    print("Welcome to Python Function")

show()
show()


def add(a,b):
    print("Sum is ",a+b)

add(10,20)
add(50,80)


def squareroot(num):
    sqrt = num*num
    return sqrt

print(squareroot(9))
print(squareroot(41))


def add(a,b=20):
    print("Sum is ",a+b)

add(10)
add(50,80)



# Anonymous Function
sum = lambda arg1, arg2: arg1+arg2;

print(sum(50,90))