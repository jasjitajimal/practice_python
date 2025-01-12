n = int(input("Enter how many numbers you want in list)"))
list1 = list(range(n))
for a in list1:
    list1[a] = int(input("Enter the number:"))

print(list1)
