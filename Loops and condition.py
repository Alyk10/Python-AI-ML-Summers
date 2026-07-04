#range and loops

#for i in range(1, 11): #1 se start hoga and then 11-1=10 tak chalega
#    print(i)
#for i in range(0, 11, 2): #0 se start hoga and then 11-1=10 tak chalega with step size of 2
#    print(i)
#for a in range(5):
    #print(a)

#while loop
 
#count=0
#while count <= 6: #colon after loop
  #  print("count is:", count)
 #   count += 2 #increment of 2 starting from 0 to 6
     
#password=" "
#while password != 'AK':
 #   password = input("Enter the password: ")
 #   if password == 'AK':
#        print("Access granted")
#    else:
#        print("Access denied")

#while True:
#    password = input("Enter the password: ")
#    if password == 'AK':
#        print("Access granted")
#        break
#   else:
#        print("Access denied")
#print("Enter two numbers to add!")
#x= input("Enter first number: ")
#y= input("Enter second number: ")
#z=int(x)+int(y) #agar int na likhein to string ke form me add hoga and output will  12 instead of 3 if we enter 1 and 2 as input
#print(z)

temp= int(input("enter temp in Celsius:"))
if temp >= 40:
    print("It's too hot!")
elif temp >= 20:
    print("It's nice!")
else:
    print("It's cold!")
