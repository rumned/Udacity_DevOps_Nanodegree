# Write your function here:
def until_dot(s):
    index = 0
    while index < len(s) and s[index] != ".":
        index += 1
    return(s[:index])
# You can test your function using the print statements below:

# This should print 'Udacity'
print(until_dot("Udacity.com"))

s = input("Test this function! Input string here:\n")
print(until_dot(s))