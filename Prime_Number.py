n = int(input("Enter a number:"))
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n** 0.5)+1):
        if(n%i == 0):
            return False
    return True
if isPrime(n):
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is a Non-Prime Number")
    