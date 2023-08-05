num1 = int(input("input the first number=="))
num2 = int(input("input the second number=="))

if num1 > num2:
    sma = num2
else:
    sma = num1

a = 1
for i in range(1, sma+1):
    if num1 % i == 0 and num2 % i == 0:
        a = i

print("the answer is==" , a)
