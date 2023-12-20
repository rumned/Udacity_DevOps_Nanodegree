import string
test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]

def bleeper(word):
    word = word.strip(string.punctuation).lower()
    bad_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]
    if word in bad_words:
        word = word.replace(word,"*"*len(word))
    return word


for word in test_words:
    print(bleeper(word)) #code deletes punctuation

# # Udacity code below
# import string # Import the string module so we can use string.punctuation
# test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]

# def bleeper(word):
#     pos = 0 # Track the position (index) of the character so we can replace it
#     for character in word:
#         if character not in string.punctuation:
#             character = "*" # If it wasn't punctuation, replace it
#         word = word.replace(word[pos], character) # Replace the character at the current position
#         pos += 1 # Move to the next character position
#     return word

# for word in test_words:
#     print(bleeper(word))