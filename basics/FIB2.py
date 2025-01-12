def fib(n):
    if n == 1:
        a = 1
        print(a)
    if n == 2:
        b = 1
        print(b)
    if n > 2:
        a = 1
        b = 1
        i = 3
        print(a)
        print(b)
        while i < n:
            m = a+b
            a = b
            b = m
            print(m)
            i = i+1


fib(100)
