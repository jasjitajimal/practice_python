import datetime
# Range is min - 0 max - 1,000,000

# Write a Python function that takes n variable as input and return m.
# M is nth number of fibonacci series.
# 1,1,2,3,5,8,13,21 ....
# EVery number is sum of last 2 number

# def

# m =


def fibonacci(n):
    m = 0
    if n >= 2:
        m = fibonacci(n - 2) + fibonacci(n-1)
    elif n == 1:
        m = 1
    elif n == 0:
        m = 1
    return m


print("\n\nRecursion Example Results")

now = datetime.datetime.now()
p = fibonacci(50)
new_now = datetime.datetime.now()
diff = abs(new_now-now).microseconds
print(f"Processing time: {diff} microseconds")
print(p)
