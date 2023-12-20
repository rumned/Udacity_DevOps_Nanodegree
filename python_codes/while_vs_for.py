# these two codes do the same thing
# but the first one uses while and second one uses if
# notice that in while we need to set the value of index and the increment too

s = "cat"
index = 0 
while index < len(s):
     print(s[index])
     index += 1
   

word = "cat"
for index in range(len(word)):
    print(word[index])
