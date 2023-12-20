d = {}
d["new"] = "Not old"
d["old"] = "Not new"
def enter_key():
    print("\n")

some_list = [1, 2, 3, 4, 5]
favorites = {'color': 'purple', 'number': 42, 'animal': 'turtle', 'language': 'python'}
# for items in favorites:
#     print(items)
# above is the default for looping over dictionaries
# which does the same thing as below:
for key in favorites.keys():
    print(key)
print("\n")
# to print the values, we have to do:
for value in favorites.values():
    print(value)
# note that it doesnt have to be "value"
# for foo in favorites.values():
#     print(foo)
print("\n")
# below is for printing the key-value pair
# this data structure is called a TUPLE- immutable
for entry in favorites.items():
    print(entry)
print("\n")
#  you can also separate them by using one loop only
for key, value in favorites.items():
    print(key)
    print(value)
# and you can do something like this
enter_key()
for key, value in favorites.items():
    print(f"My favorite {key} is {value}")
enter_key()
str = 'it appears that the the appears the most in the sentence'
dict = {}
x = str.split()
print(x)
enter_key()
  
for word in x:
    if word in dict: # since dict is empty, the first time the code runs, this part will be passed over first
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
enter_key()
for key, value in dict.items():
    if value != 1:
        print(f"The word '{key}' appears {value} "
          "times in the string")
        enter_key()
    else:
       print(f"The word '{key}' appears {value} "
          "time in the string")
       enter_key() 