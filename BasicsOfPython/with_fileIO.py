with open("newfile.txt", "r") as f:

    data = f.read()

    print(data)

    # f.close not imp BCZ closes File Automatically in with usage

with open("demo.txt", "w") as f:

        f.write("KemCheeMata")

