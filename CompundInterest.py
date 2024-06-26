principle= 0
rate=0
time=0

while True:
    principle = float(input("Enter the Principle Amount: "))
    if principle <0:
        print("Principle cannot be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate: "))
    if rate <0:
        print("Interest Rate cannot be less than or equal to zero.")
    else:
        break

while True:
    time = int(input("Enter the Time(in Years): "))
    if time <0:
        print("Time cannot be less than or equal to zero.")
    else:
        break

print(f"The Principal amount is: {principle}")
print(f"The interest rate is: {rate}")
print(f"The time in years is: {time}")

Compound_Interest = principle * ((1 + rate/100)** time)
print(f"The Compound Interest after {time} years is: {Compound_Interest:.2f}")
