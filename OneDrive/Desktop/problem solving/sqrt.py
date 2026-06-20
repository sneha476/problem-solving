# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
x=4
if x<2:
    print(x)
elif x==2:
    print("1")
for i in range(x):
    if i*i>x:
        print(i-1)
