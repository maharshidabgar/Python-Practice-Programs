# Write a Recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):

    if (n == 1): # Base - Case

        return 1

    return n + cal_sum(n-1) # Recursive - Call

n = int(input("Enter a Number : "))

print("Sum =",cal_sum(n))