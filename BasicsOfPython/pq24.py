# WAF to print the elements of a list in a siingle line. (list is the parameter)

single = [78, 52, 45, 12, 68]

sec = [True, False, 78.91, "RamRam"]

def print_sing(single):

    for item in single:

        print(item, end= " ")

print_sing(sec)  

print_sing(single)