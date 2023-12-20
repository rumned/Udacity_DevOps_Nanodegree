
# def remove_spam(string,spam):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index+len(spam)] == spam :
#             index += len(spam)
#         else:
#             output.append(string[index])
#             index += 1
#     return"".join(output)

# print (remove_spam('SPAM!HelloSPAM! worldSPAM!!','SPAM!'))
# string = input("Enter your string: ")
# spam = input("Enter the target: ")
# print(remove_spam(string,spam))

# below is Udacity code
# def remove_substring(string, substring):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index+len(substring)] == substring:
#             index += len(substring)
#         else:
#             output.append(string[index])
#             index += 1
#     return "".join(output)

# # Here are some strings you can test your function:
# print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
# print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
# print(remove_substring('I am NOT learning to code.', 'NOT '))

#replace
def replace_spam(string,spam,replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(spam)] == spam :
            output.append(replacement)
            index += len(spam)
        else:
            output.append(string[index])
            index += 1
    return"".join(output)

print (replace_spam('SPAM!HelloSPAM! worldSPAM!!','SPAM!',""))
string = input("Enter your string: ")
spam = input("Enter the target: ")
replacement = input("Enter the real word: ")
print(replace_spam(string,spam,replacement))

# udacity code below
# def replace_substring(string, substring, replacement):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index+len(substring)] == substring:
#             output.append(replacement)
#             index += len(substring)
#         else:
#             output.append(string[index])
#             index += 1
#     return "".join(output)