def Factorial_Number (number):

    factorial = 1

    if number == 0:
        return factorial
    else:
        for i in range(1 , number + 1):
            factorial = factorial * i
    print(factorial)

number = int(input("Please enter a number: "))

Factorial_Number(number)