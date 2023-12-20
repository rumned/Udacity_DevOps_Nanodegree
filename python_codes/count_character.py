# count = 0
# for ch in "bonobos":
#     if ch == "o":
#         count = count + 1


# this is the function using if
def count_character(string,char):
    count = 0
    for ch in string:
        if ch == char:
            count = count + 1
    return count

# the same function using while
def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1 #this is for the number of same characters
        index += 1 #we increase the position by 1
    return total

# These print statements will call the function to test different strings and print out the returned results. 
# (You can comment-them-out with a # if they are getting in your way.)
print("Should print a count of 3:")
print(count_character("oxen and foxen all live in boxen", "x"))

print("Should print a count of 0:")
print(count_character("that letter isn't here", "x"))

print("Should print a count of 9:")
print(count_character("the goofy doom of the balloon goons", "o"))

print("Should print a count of 6:")
print(count_character("papa pony and the parcel post problem", "p"))

print("Should print a count of 0:")
print(count_character("this bunch of words has no", "e"))

string = input("Now try it yourself. Enter the sentence you want to check:\n")
target = input("What is the character you want to check?\n")
print(count_character(string,target))

# adding another check here to see if the input would break the code
print("Should print a count of 0:")
print(count_character("this bunch of words has no", "e"))