# WAF to find in which line of the file does the word "learning" occur
# first. Print - 1 if word nnot found...

def check_line_word():

    word = "leing"

    data = True

    line_no = 1

    with open("practice.txt", "r") as f:

        while data:

            data = f.readline()

            if word in data:

                print(line_no)
                return

            line_no += 1

    return -1

print(check_line_word())