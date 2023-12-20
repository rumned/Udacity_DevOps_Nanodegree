# Write your function definition here.
def starts_with(long,short):
    if long[0:len(short)] == short :
        return True
    return False
# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))