import math

def sqrt_root(x):
    return math.sqrt(x)

res = sqrt_root(4)
print(res)

square_root = lambda x: math.sqrt(x)

res = square_root(4)
print(res)

print("---------------------")

def make_adder(n):
    return lambda x: x + n

adder2 = make_adder(2)
val = adder2(5)
print(val)


adder3 = make_adder(4)
val = adder3(5)
print(val)