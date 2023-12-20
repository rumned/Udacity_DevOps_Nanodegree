def locate_all(string, target):
    index = 0
    matches = []
    while index < len(string):
        if string[index : index + len(target)] == target:
            matches.append (index)
            index += len(target) #this line causes this function to not overlap
        else:
            index += 1
    return matches

# Here are a couple function calls to test with.

print("This one should return 1,5")
print(locate_all('cookbook', 'ook'))

string = input("String: ")
target = input("Substring: ")

print(locate_all(string,target))