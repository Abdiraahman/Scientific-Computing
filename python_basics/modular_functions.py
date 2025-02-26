import math # Importing math module to access math.pi


# Function to calculate the area of different shapes
def calculate_area(shape,dimension1,dimension2=0):
    match shape:
        case "circle":
            return math.pi * dimension1**2
        case "rectangle":
            return dimension1 * dimension2
        case "triangle":
            return 0.5*dimension1*dimension2

        case _:
            return "Invalid shape"


# Calculating the area of different shapes

circleArea = calculate_area("circle",14) #Area of circle

rectArea = calculate_area("rectangle",15,6)  #Area of rectangle

triangleArea = calculate_area("triangle",10,5)  #Area of triangle

area = calculate_area("square",9) #Area of invalid shape

# Printing the calculated areas

print(f'Circle: {circleArea}')

print(f'Rectangle: {rectArea}')

print(f'Triangle: {triangleArea}')

print(f'Any other: {area}')



