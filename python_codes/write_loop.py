with open("new_file.txt", "w") as new_file:
    for num in range(31):
        if num % 2 == 0:
            new_file.write(str(num))
            new_file.write("\n")