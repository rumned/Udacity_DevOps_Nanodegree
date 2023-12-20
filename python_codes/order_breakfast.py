import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(0.5)
print("Today we have two breakfasts available.")
time.sleep(0.5)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(0.5)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(0.5)
def order_food():
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(1)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(1)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(1)
    print("Your order will be ready shortly.")
    time.sleep(0.5)    
    def order_again():
        while True:
            response_again = input("Would you like to order again?\n"
                            "Please type 'yes' or 'no',I would not understand other words.\n").lower()
            if "yes" in response_again:
                time.sleep(0.5)
                order_food()
            elif "no" in response_again:
                time.sleep(0.5)
                print("Thanks for having breakfast with me!")
                break
            else:
                print("Sorry, I don't understand.")
                time.sleep(1)
                order_again()
            break
    order_again()

order_food()

# # udacity solution below

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
#     while True:
#         response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
#         if "waffles" in response:
#             print("Waffles it is!")
#             time.sleep(2)
#             break
#         elif "pancakes" in response:
#             print("Pancakes it is!")
#             time.sleep(2)
#             break
#         else:
#             print("Sorry, I don't understand.")
#             time.sleep(2)
#     print("Your order will be ready shortly.")
#     time.sleep(2)
#     while True: # We want to loop until they enter a valid response.
#         order_again = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
#         if 'no' in order_again:
#             print("OK, goodbye!")
#             time.sleep(2)
#             break # Note that this will only break out of the inner loop.
#         elif 'yes' in order_again:
#             print("Very good, I'm happy to take another order.")
#             time.sleep(2)
#             break # Again, this only breaks out of the inner loop.
#         else:
#             print("Sorry, I don't understand.")
#             time.sleep(2)
#     if 'no' in order_again: 
#         break # We need this last break statement to exit the outer loop.