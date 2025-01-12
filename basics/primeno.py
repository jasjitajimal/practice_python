a = int(input("Enter any number:"))
if a == 1:
    x = " {} is not prime number"
    print(x.format(a))
elif a > 1:
    for i in range(2, a):
        if a % i == 0:
            print(a, " is not prime number")
            print(i, " times", a/i, "is", a)
            break
    else:
            print(a, "is prime number")
else:
    print(a, " is not prime number")
