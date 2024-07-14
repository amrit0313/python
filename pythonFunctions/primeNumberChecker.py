def primeNumberChecker(number):
    isPrime = True
    for n in range(2, number-1):
        if  number%n ==0:
            isPrime = False

    if isPrime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")            

n = int(input("Enter the number to check: "))
primeNumberChecker(n)