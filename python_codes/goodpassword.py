def good_length (pw):
    return len(pw) > 7 and len(pw) < 65


word = input("Enter password: \n")
print(good_length(word))

