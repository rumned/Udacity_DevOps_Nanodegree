# def is_substring(string,substring):
#     for n in range(len(string)):
#         if string[n : n + len(substring)] == substring:
#             print (substring +" found in " + string) #this part works but I could not write a false situation
     

# # below is Udacity code
# def is_substring(substring, string):
#     index = 0
#     while index < len(string):
#         if string[index : index + len(substring)] == substring:
#             return True
#         index += 1
#     return False

# string = input("String: ")
# substring = input("Substring: ")

# print(is_substring(string,substring))

#code does not work as intended

def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        # if string[index : index + len(target)] == target:
        #     total += 1
        # index += 1 
        
        #if you dont want to allow overlap use the code below
        if string[index : index + len(target)] == target:
            total += 1
        index += len(target)
    else:
        index += 1
    return total

string = input("String: ")
target = input("Substring: ")

print(count_substring(string,target))