import time
import colorama
from colorama import Fore

colorama.init()

# Prompt the user for their decision
decision = input("Welcome to Aahan's Restaurant! Would you like to order something? ").lower()

# Validate the decision input
if decision not in ["yes", "no"]:
    decision = input("Please enter yes or no: ").lower()

# If the decision is "no", exit the program
if decision == "no":
    print("Okay, see you later!")
    exit()

# Define the drink menu items with their descriptions and prices
Drink_Menu = [
    "Espresso: $3, A concentrated shot of pure coffee \n",
    "Cappuccino: $4, Espresso with steamed milk and foam \n",
    "Latte: $5, Espresso with steamed milk and a light layer of foam \n",
    "Americano: $3, Espresso diluted with hot water \n",
    "Hot Chocolate: $2, A rich, creamy chocolate beverage \n",
    "Tea: $2, A variety of hot tea options \n",
    "Milk Shake: $3, A thick, cold beverage made with milk and ice cream \n",
    "Mocha: $4, Espresso with steamed milk and chocolate \n",
    "Coffee: $3, A classic brewed coffee \n",
]

# Define the food menu items with their descriptions and prices
Food_Menu = [
    "French Fries: $5, Crispy, golden-brown fried potato strips \n",
    "Burger: $10, A sandwich with a patty, bun, and various toppings \n",
    "Pizza: $15, A flatbread topped with tomato sauce, cheese, and various toppings \n",
    "Chicken Wings: $5, Crispy, saucy chicken wings \n",
    "Sandwich: $7, A variety of fillings between two slices of bread \n",
    "Pasta: $15, Various types of pasta dishes \n",
    "Risotto: $15, A creamy, rice-based dish with vegetables or meat \n",
    "Ramen: $20, A Japanese noodle soup with broth, noodles, and toppings \n",
    "Sushi: $25, Vinegared rice rolls with various fillings \n",
]
