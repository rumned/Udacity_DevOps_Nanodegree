def start_K(s):
    if s[0] == "K":
        return "True"
    elif s[0] == "k":
        return "Yes!"
    else:
        return "No :("
    
string = input("Check if this string starts with the letter k: ")
print (start_K(string))
