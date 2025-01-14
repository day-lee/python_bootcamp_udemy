MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. User input asking the menu
# TODO: 2. Turning off for maintenance
# TODO: 3. Check resources using report
# TODO: 4. Check enough resources to make coffee

def resource_check(drink, ingredient_type):
    '''returns booleans after comparison between needed ingredients and left resources'''
    ingredients_check = MENU[drink]['ingredients'][ingredient_type]
    resources_check = resources[ingredient_type]

    if ingredients_check <= resources_check:
        return True
    elif ingredients_check > resources_check:
        return False

def check(water_check, milk_check, coffee_check):
    '''returns boolean on each steps including amount of ingredients and customer's payment '''
    if water_check:
        if milk_check:
            if coffee_check:
                print('Please insert coins.')
                return True
            else:
                print(f"Sorry there is not enough coffee.")
        else:
            print(f"Sorry there is not enough milk.")
    else:
        print(f"Sorry there is not enough water.")
    coffee_serving()

# TODO: 5. Input coins by user
def money(name_of_coins):
    '''gets each coins amount for payment '''
    ask_money = int(input(f"how many {name_of_coins}?: "))
    return ask_money
#
# TODO: 6. Calculate transaction
def calculate_transaction(money_insufficient, give_change, same, change):
    '''returns booleans after money calculation '''
    if money_insufficient:
        print("Sorry that's not enough money. Money refunded.")
        continue_serving = False
    elif give_change:
        print(f"Here is ${change} dollars in change.")
        return True
    elif same:
        return True
# TODO: 7. Add profit before making coffee
# TODO: 8-1. Make coffee deduct ingredients
def ingredients_deduction(drink, ingredient_type):
    '''deduct amount of ingredients from existing resources'''
    resources[ingredient_type] -= MENU[drink]['ingredients'][ingredient_type]

#TODO: 8-2.  Print serving
#TODO: 10. serve the next customer by repeating from todo1

def coffee_serving():
    '''a program to serve a customer for drinks'''
    continue_serving = True
    profit = 0
    while continue_serving:
        ask_menu = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if ask_menu == "report":
            print(f"Water : {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}")
        elif ask_menu == 'off':
            continue_serving = False
        elif ask_menu == 'latte' or ask_menu == 'cappuccino' or ask_menu == 'espresso':
            #resource checked
            water_check = resource_check(ask_menu, 'water')
            coffee_check = resource_check(ask_menu, 'coffee')
            milk_check = resource_check(ask_menu, 'milk')
            if check(water_check, milk_check, coffee_check):
                quarters = money("quarters")
                dimes = money("dimes")
                nickles = money("nickles")
                pennies = money("pennies")
                
                user_money = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
                print(f'    given money:{user_money}')
                change = round((user_money - MENU[ask_menu]["cost"]), 2)
                money_insufficient = (user_money < MENU[ask_menu]["cost"]) #bool True
                give_change = (user_money > MENU[ask_menu]["cost"])
                same = (user_money == MENU[ask_menu]["cost"])

                if calculate_transaction(money_insufficient, give_change, same, change): #enoug or same
                    profit += MENU[ask_menu]["cost"]
                    print(f'    total profit:{profit}')
                    ingredients_deduction(ask_menu, 'milk')
                    ingredients_deduction(ask_menu, 'water')
                    ingredients_deduction(ask_menu, 'coffee')
                    print(f'    remaining resources:{resources}')
                    print(f'"Here is your {ask_menu} ☕ Enjoy!"')
coffee_serving()
