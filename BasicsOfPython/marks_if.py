marks = int(input("Enter Student's Marks for Grade : "))

if (marks >= 90):
    print("Grade is A")

elif (marks >= 80 and marks < 90):
    print("Grade is B")

elif (marks >= 70 and marks < 80):
    print("Grade is C")

elif (marks < 70):
    print("Grade is D")

else:
    print("Faill !!!")