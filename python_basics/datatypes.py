
# Defining variables of different data types

num1=7     # integer
float1=12.5  # float
complex1=3+5j   # complex number
list1 = [27,3,8]  # list
tuple1 = (18,3,4)  # tuple
dict1= {'Ali':22, 'seph':18}  # dictionary
set1 = {1,2,6} # set
bool1 = True   # boolean

# Printing the type of each variable using formatted string
print(f" num1: \t\t{type(num1)}\n float1: \t{type(float1)}\n complex1: \t{type(complex1)}\n list1:\t\t{type(list1)}\n tuple1: \t{type(tuple1)}\n dict1:\t\t{type(dict1)}\n set1: \t\t{type(set1)}\n bool1:\t\t{type(bool1)}\n")

# Type conversion examples
float2 = float(num1)  # Converting integer to float
num2 = int(float1)   # Converting float to integer

# Printing converted values
print(f"num2: \t{num2}\nfloat2: {float2}") 