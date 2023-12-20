# # handle_bad_input udacity code

# while True:
#     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#     if response == "waffles":
#         print("Waffles it is!")
#         break
#     elif response == "pancakes":
#         print("Pancakes it is!")
#         break
#     else:
#         print("Sorry, I don't understand.") #this code only handles exact input of waffles/pancakes

# response = ""
# while response != "waffles" and response != "pancakes":
#     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#     if response == "waffles":
#         print("Waffles it is!")
#     elif response == "pancakes":
#         print("Pancakes it is!")
#     else:
        # print("Sorry, I don't understand.") #same here, only handles exact input.

# this code can at least scan a string
# while True:
#     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#     if "waffles" in response:
#         print("Waffles it is!")
#         break
#     elif "pancakes" in response:
#         print("Pancakes it is!")
#         break
#     else:
#         print("Sorry, I don't understand.")
## end of udacity code

# this code does not repeat intro

intro = ("""Hello! I am Bob, the Breakfast Bot.\n
Today we have two breakfasts available.\n
The first is waffles with strawberries and whipped cream.\n
The second is sweet potato pancakes with butter and syrup.""")

intro_count = 0
while intro_count <= 0:
    print(intro)
    intro_count += 1
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")
print("Your order will be ready shortly.") # This one is also outside the loop!
# end of doesnot repeat intro

# order_count = 0
# response_count = 0
# while order_count > 0:
#     break 
# while response_count < 0:
#     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#     if "waffles" in response:
#         print("Waffles it is!")
#         response_count += 1
#         break
#     elif "pancakes" in response:
#         print("Pancakes it is!")
#         response_count += 1
#         break 
#     else:         
#         print("Sorry, I don't understand.")

# order_ready = "Your order will be ready shortly."
# print (order_ready)
# order_count += 1

# below code is for adding pause
# import time

# print("Hello! I am Bob, the Breakfast Bot.")
# time.sleep(2)
# print("Today we have two breakfasts available.")
# time.sleep(2)
# print("The first is waffles with strawberries and whipped cream.")
# time.sleep(2)
# print("The second is sweet potato pancakes with butter and syrup.")
# time.sleep(2)

# while True:
#     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#     if "waffles" in response:
#         print("Waffles it is!")
#         time.sleep(2)
#         break
#     elif "pancakes" in response:
#         print("Pancakes it is!")
#         time.sleep(2)
#         break
#     else:
#         print("Sorry, I don't understand.")
#         time.sleep(2)
# print("Your order will be ready shortly.")
# time.sleep(2)

