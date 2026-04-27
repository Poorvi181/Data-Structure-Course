n = 4

for i in range(1, n + 1):
    print("*" * i)
#Keep taking numbers until user enters 0: Print running total each time
total = 0
while True:
    num=int(input("Enter number(type 0 to stop): "))
    if num == 0:
        break
    total+=num
    print("Running total", total)

# #Take a number n and: Print numbers from 1 to n
# For multiples of 3 → print "Fizz"
# For multiples of 5 → print "Buzz"
# For both → print "FizzBuzz"

n=int(input("Pick a number: "))

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


