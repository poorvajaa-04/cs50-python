'''
Even if you haven't studied physics (recently or ever!), you might have heard that E =mc2, wherein E represents energy 
(measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 
300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then 
outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

'''

c = 300000000
m = int(input("Enter the mass of the object in kilograms: "))

E = m*(c**2)
print(E)

