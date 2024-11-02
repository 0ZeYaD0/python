import os

os.system("cls")

menu = {"pizza":5.00,
        "s popcorn": 2.50,
        "m popcorn": 3.50,
        "l popcorn":4.00,
        "nacho":3.00,
        "coke":1.50,
        "fries": 4.50,
        "chips":1.00,
        "lemonade":1.50}

cart = []
total = 0

print("----------------- MENU -----------------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------------------")

while True:
    food = input("Select what do you want (q to quit):").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
if cart:
    print("----------------- YOUR ORDER -----------------")
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print(f"The total is: ${total:.2f} ")