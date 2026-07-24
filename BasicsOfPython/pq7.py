num1 = int(input("Enter 1st Num : "))
num2 = int(input("Enter 2nd Num : "))
num3 = int(input("Enter 3rd Num : "))

if (num1 >= num2 and num1 >= num3):

    print("Greatest number is ",num1)

elif (num2 >= num1 and num2 >= num3):

    print("Greatest number is ", num2)

else:

    print("Greatest number is ", num3)