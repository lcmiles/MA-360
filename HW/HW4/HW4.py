import math
import numpy

# 1.6.2 Problem 6

radius = 5
height = 3

surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height # SA = 2πr + 2πrh

volume = math.pi * radius**2 * height # V = π * r^2 * h

print("Problem 6:")
print("")
print("The surface area of the cylinder is:", surface_area)
print("The volume of the cylinder is:", volume)
print("")

# 1.6.2 Problem 7

x1, y1 = 3, 4
x2, y2 = 5, 9

slope = (y2 - y1) / (x2 - x1) # m = (y2 - y1) / (x2 - x1)

print("Problem 7:")
print("")
print("The slope between the two points is:", slope)
print("")

# 1.6.2 Problem 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # distance = √(x2-x1)^2 + (y2-y1)^2

print("Problem 8:")
print("")
print("The distance between the two points is:", distance)
print("")

# 1.6.2 Problem 9

factorial = math.factorial(6)

print("Problem 9:")
print("")
print("Factorial of 6 is:", factorial)
print("")

# 1.6.2 Problem 11

approximation_N0 = 1 / (2 * math.sqrt(2) / 9801 * 1103) # Ramanujan's formula for N = 0

approximation_N1 = 1 / (2 * math.sqrt(2) / 9801 * (1103 + 26390/396)) # Ramanujan's formula for N = 1

true_pi = math.pi

print("Problem 11:")
print("Ramanujan's approximation for N = 0 is:", approximation_N0)
print("Ramanujan's approximation for N = 1 is:", approximation_N1)
print("MATLAB's pi value is:", true_pi)
print("")

# 1.6.2 Problem 14

angle_radians = math.radians(87)
sin_87_degrees = math.sin(angle_radians)

print("Problem 9:")
print("")
print("The sine of 87˚ is:", sin_87_degrees)
print("")

# 5.4 Problem 5

def my_mat_mult(P, Q):
    m, p = P.shape # Gets the shape of the matrix P (m rows, p columns)
    l, n = Q.shape # Gets the shape of the matrix Q (l rows, n columns)
    
    if p != l:
        raise ValueError("Inner dimensions do not match for matrix multiplication") # Cannot multiply matrices that do not have matching dimensions
    
    M = numpy.zeros((m, n),dtype=int) # Initialize matrix of int zeros to store result
    
    for i in range(m): # Iterate over rows in P
        for j in range(n): # Iterate over columns in Q
            for k in range(p): #Iterate over number of columns in P and rows in Q
                M[i, j] += P[i, k] * Q[k, j] # Calculate the element using matrix multiplication 
    
    return M

# Test cases
print("Problem 9:")
print("")
P = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
Q = numpy.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print("Array P:")
print(P)
print("Array Q:")
print(Q)
print("Array PQ:")
print(my_mat_mult(P, Q))
print("")
