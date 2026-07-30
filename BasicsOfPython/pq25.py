# WAF to find the Factorial of n. (n is the parameter)

def cal_fact(n):

    fact = 1 # Do not fact = 0 BCZ 

    for i in range(1, n+1):

        fact *= i

    print(fact)

    return fact

cal_fact(6)