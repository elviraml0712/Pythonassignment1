#Input the Two Numbers
num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))

#Check which number is smaller
if num1 < num2:
    min_num = num1
else:min_num = num2

print("////////////////////////////////")

#Print the Minimun Number  sdfgdf
print("The Minimun Number is", min_num)

radius = int(input("Enter Radius : "))
if radius <= 5:
    print("The Entered Radius is OK!")
else: 
    print("The Entered Radius is too big!")

print("////////////////////////////////")

age = int(input("How Old are you? : "))
if age == 32:
    print("You can eligible to buy Canabis!")
elif age <=12:
    print("Sorry you are too young!")
else: 
    print("Sorry you are too old!")

print("////////////////////////////////")

num = int(input("Enter your Number : "))
if (num % 2) == 0:
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))

print("////////////////////////////////")

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print("Welcome", fname + lname)


print("////////////////////////////////")

id = int(input("Enter your ID: "))
name = input("Enter your Name: ")
print("My name is " + name + " and my ID is " + str(id))

print("////////////////////////////////")

firstnum = int(input("Enter first value"))
secondnum = int(input("Enter second value"))
operator = input("operator (+ *)")
try:
    output = True

    if operator == "+":
        result = firstnum + secondnum
    elif operator == "*":
        result = firstnum * secondnum

    else:
        output = False
        print("Wrong Operator")

    if output:
        print("Result is", result)

except ValueError:
    print("Please enter number only")
    print(ValueError)


