x = int(input("Enter first number\n"))
y = int(input("Enter second number\n"))

z = int(input("Enter the result\n"))

if (x + y) == z:
    print(x, " + ", y, " = ", z)
elif (x - y) == z:
    print(x, " - ", y, " = ", z)
elif (x * y) == z:
    print(x, " * ", y, " = ", z)
elif (x / y) == z:
    print(x, " / ", y, " = ", z)
elif (x % y) == z:
    print(x, " % ", y, " = ", z)
elif (x ** y) == z:
    print(x, " ^ ", y, " = ", z)
