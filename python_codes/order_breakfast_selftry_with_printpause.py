import time

def print_pause(message):
    print(message)
    time.sleep(0.8)

# need to define this into intro function
print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

# need to add valid input function
def order_food():
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, I don't understand.")
            
    print_pause("Your order will be ready shortly.")   
    def order_again():
        while True:
            response_again = input("Would you like to order again?\n"
                            "Please type 'yes' or 'no',I would not understand other words.\n").lower()
            if "yes" in response_again:
                time.sleep(0.5)
                order_food()
            elif "no" in response_again:
                time.sleep(0.5)
                print_pause("Thanks for having breakfast with me!")
                break
            else:
                print_pause("Sorry, I don't understand.")
                order_again()
            break
    order_again()

order_food()

# need to add order_breakfast function