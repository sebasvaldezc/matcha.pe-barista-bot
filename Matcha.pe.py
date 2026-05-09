#Order online at matcha.pe store

#---------------------------------------------------- Welcome! in TUPLE format
import time

welcome_message = (
    "\nWelcome to Matcha.PE",
    """
█▀▄▀█ ▄▀█ ▀█▀ █▀▀ █░█ ▄▀█ ░  █▀█ █▀▀
█░▀░█ █▀█ ░█░ █▄▄ █▀█ █▀█ ▄  █▀▀ ██▄
    """,#<--- I used here a multi-line-string to have the space
    "Your one stop shop for all things with matcha!\n"
)

def welcome():
    for line in welcome_message:
        print(line)

welcome()
#---------------------------------------------------- Name + Evil Check Lol
name = input("¿What's your name?\n").title()

if name.lower() in ["none","unknown","nadie", "a"]:
    evil_status = input("Mmmm, are you evil? (yes/no)\n")
    if evil_status.lower() in ["yes","y"]:
        print("\n Sorry, but you're not welcome here, get out!\n")
        exit()
    else:
        print("\nHi" + name + ",thanks for coming today\n")

else:
    print("\nHi " + name + ", thanks for coming today :)")

#---------------------------------------------------- Menu Text
menu = ("""
╔════════════════════════════╗
        MATCHA.PE MENU
╚════════════════════════════╝

1. Matcha Original   - $6
2. Matcha Strawberry - $6
3. Matcha Mocha      - $6
4. Matcha Mango      - $8
5. Matcha Ice Cream  - $10

══════════════════════════════
""")

print(menu)

#---------------------------------------------------- Price + Order
while True:
    order = input("¿What would you like to order?\n")

    if order.lower() in ["1", "1.", "1)", "original", "matcha original", "original matcha"]:
        price = 6
        drink = "Matcha Original"
        break

    elif order.lower() in ["2", "2.", "2)", "strawberry", "strawberry matcha", "matcha strawberry"]:
        price = 6
        drink = "Matcha Strawberry"
        break

    elif order.lower() in ["3", "3.", "3)", "mocha", "mocha matcha", "matcha mocha"]:
        price = 6
        drink = "Matcha Mocha"
        break

    elif order.lower() in ["4", "4.", "4)", "mango", "matcha mango", "mango matcha"]:
        price = 8
        drink = "Matcha Mango"
        break

    elif order.lower() in ["5", "5.", "5)", "ice cream", "matcha ice cream", "ice cream matcha"]:
        price = 10
        drink = "Matcha Ice Cream"
        whippe_cream = input ("\nWould you like to add whipped cream for an extra $2? (yes/no)\n")
        if whippe_cream.lower() in ["yes", "y"]:
            price += 2
            drink += " with whipped cream"
        break

    elif order.lower() in ["exit","salir","nothing","nada","ya no","no more"]:
        print("\nThat's fine, welcome back anytime!\n")
        exit()

    else:
        print("\nSorry, we don't have that on the menu. Please try again.\n")
        price = 0

#---------------------------------------------------- Copies + "Valid Number"
print("\n---- Good choice, " + name + "! ----\n" "Your " + drink + " will be ready soon.\n") 

while True:
    copies = input("How many copies would you like?\n")

    try:
        copies = int(copies)

        if copies > 0:
            break
        else:
            print("Please enter a number greater than 0.\n")

    except ValueError:
        print("Please enter a valid number.\n")

#---------------------------------------------------- Final Total
total = int(copies) * price

print(f"---- Your total is: ${total} ----") 
print("Thank you for your order " + name + "\n")

#+ "----\n" "Thank you for ordering, " + name + "!\n")

#---------------------------------------------------- Delivery or Pick Up?

while True:
    method = input("---- Delivery or Pick Up? ----\n").lower()

    if method.lower() in ["pick up", "pickup", "pick-up", "p"]:

        print("\nPreparing your order", end="")
        for i in range(3): 
            time.sleep(0.7) 
            print(".", end="", flush=True)

        print("\n""""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Your order is ready to be picked up, enjoy! :D 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        break
        
    elif method.lower() in ["delivery", "d"]:
        print("\nPreparing your order", end="")
        for i in range(3): 
            time.sleep(0.7) 
            print(".", end="", flush=True)
        
        print("\n" + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Your order is on the way, enjoy! :D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        break

    elif method.lower() in ["exit", "salir", "nada", "cancel"]:
        print("\nThat's fine, welcome back anytime!\n")
        exit()

    else:
        print("Invalid delivery method.")





