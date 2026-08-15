# LAB TASK 1 by Ali Khan
#q1 printing the list of colors and printing them
colors=["red", "green", "blue","yellow"]
#print(colors)

#q2 adding new color to the list
colors.append("orange")
print(colors)

#q3removing green from the list
colors.remove("green")
print(colors)

#q4 reverse using slicnig
print(colors[::-1])

#q4 print staric in reverse order using for loop
for i in range(6,0,-1):
    print("*"*i) # *i is the number of times it occurs ;6

# q5 while loop
n = int(input("Enter a positive integer: "))
while n > 0:
    print("Well Done")
    n -= 1

#q6 take input from user and multiply
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Product:", num1 * num2)

temp= int(input("enter temp:"))
if temp >= 35:
    print("Hot Weather")
elif temp < 35 and temp >= 25:
    print("Happy Day")
else:
    print("Cold Day")
