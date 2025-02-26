
# Function to check if a number is even
def checkEven(number):
    if number % 2==0: # if remainder is zero, it is even
        return True
    else:            # Otherwise, it's odd 
        return False

# Taking user input and convert to an integer
num1=int(input('Enter an integer: '))

# Check if the number is even or odd and print the result
if checkEven(num1):
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

#printing even numbers between 1 and 50 inclusive using for loop
even_numbers=[]
for i in range(1,51):
    if checkEven(i):
        even_numbers.append(i)

print(even_numbers)

#print numbers from 10 down to 1 in reverse order
number1=10
while number1>0:
    print(number1)
    number1-=1

