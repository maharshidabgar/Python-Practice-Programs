# Write a Recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(list, idx = 0):

    if(idx == len(list)):

        return

    print(list[idx])

    print_list(list, idx+1)

list = ["Bhavnagar", "Palitana", "Mahuva", "Dahod", "Vapi"]

print_list(list)
