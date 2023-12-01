lv = int(input("Enter lower Interval:"))
u = int(input("Enter upper Interval:"))
print(" Armstring numbers in intervals are:")
for num in range(lv, u+1):
    order = len(str(num))
    sum = 0
    num1 = num
    while num1 > 0:
        digit = num1 % 10
        sum = sum + digit**order
        num1 = num1 // 10

    if sum == num:
        print(num)
