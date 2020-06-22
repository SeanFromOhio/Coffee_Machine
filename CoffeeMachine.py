# CoffeeMachine - A program that mimics the functionality of an advanced coffee machine with multiple
# ways of interacting with the program. First real attempt at OOP.


class CoffeeMachine:

    water_level = 400      # The water level in the coffee machine (Class attribute)
    milk_level = 540       # The milk level in the coffee machine (Class attribute)
    bean_level = 120       # The bean level in the coffee machine (Class attribute)
    disposable_cups = 9    # The cup level in the coffee machine (Class attribute)
    money = 550            # The amount of money currently in the machine (Class attribute)

    def __init__(self):
        self.ui()   # Initializing the ui method by calling the class, no declared instances variables here.

    def ui(self):   # The method that handles user input, and is the "menu" so to speak.
        command = input("Write action (buy, fill, take, remaining, exit): ")
        self.operations(command)

    def operations(self, command):  # This is the processing method that handles all the operations

        if command == "exit":   # An option to stop the program [OFF BUTTON]
            return None

        if command == "remaining":  # An option to show the resource level within the machine including money
            print(f"""
The coffee machine has:
{CoffeeMachine.water_level} ml of water
{CoffeeMachine.milk_level} ml of milk
{CoffeeMachine.bean_level} g of coffee beans
{CoffeeMachine.disposable_cups} of cups
{CoffeeMachine.money} of money
""")
            self.ui()   # This simply reverts back to the ui method after this method has run to completion

        elif command == "buy":  # An option to buy a coffee (3 types)
            print("Make a drink choice: 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            drink_choice = input()

            if drink_choice == "1":    # It checks that there are enough resources then makes the coffee and subtracts
                                       # the amount of resources needed to make it and the money gained
                if (CoffeeMachine.water_level >= 250 and CoffeeMachine.bean_level >= 16
                        and CoffeeMachine.disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!\n")
                    CoffeeMachine.water_level -= 250
                    CoffeeMachine.bean_level -= 16
                    CoffeeMachine.money += 4
                    CoffeeMachine.disposable_cups -= 1
                    self.ui()

                else:

                    if CoffeeMachine.water_level < 250:
                        print("Sorry, not enough water!\n")
                        self.ui()

                    elif CoffeeMachine.bean_level < 16:
                        print("Sorry, not enough beans!\n")
                        self.ui()

                    elif CoffeeMachine.disposable_cups < 1:
                        print("Sorry, not enough cups!\n")
                        self.ui()

            elif drink_choice == "2":

                if (CoffeeMachine.water_level >= 350 and CoffeeMachine.milk_level >= 75
                        and CoffeeMachine.bean_level >= 20 and CoffeeMachine.disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!\n")
                    CoffeeMachine.water_level -= 350
                    CoffeeMachine.milk_level -= 75
                    CoffeeMachine.bean_level -= 20
                    CoffeeMachine.money += 7
                    CoffeeMachine.disposable_cups -= 1
                    self.ui()

                else:

                    if CoffeeMachine.water_level < 350:
                        print("Sorry, not enough water!\n")
                        self.ui()

                    elif CoffeeMachine.milk_level < 75:
                        print("Sorry, not enough milk!\n")
                        self.ui()

                    elif CoffeeMachine.bean_level < 20:
                        print("Sorry, not enough beans!\n")
                        self.ui()

                    elif CoffeeMachine.disposable_cups < 1:
                        print("Sorry, not enough cups!\n")
                        self.ui()

            elif drink_choice == "3":

                if (CoffeeMachine.water_level >= 200 and CoffeeMachine.milk_level >= 100
                        and CoffeeMachine.bean_level >= 12 and CoffeeMachine.disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!\n")
                    CoffeeMachine.water_level -= 200
                    CoffeeMachine.milk_level -= 100
                    CoffeeMachine.bean_level -= 12
                    CoffeeMachine.money += 6
                    CoffeeMachine.disposable_cups -= 1
                    self.ui()

                else:

                    if CoffeeMachine.water_level < 200:
                        print("Sorry, not enough water!\n")
                        self.ui()

                    elif CoffeeMachine.milk_level < 100:
                        print("Sorry, not enough milk!\n")
                        self.ui()

                    elif CoffeeMachine.bean_level < 12:
                        print("Sorry, not enough beans!\n")
                        self.ui()

                    elif CoffeeMachine.disposable_cups < 1:
                        print("Sorry, not enough cups!\n")
                        self.ui()

            elif drink_choice == "back":
                self.ui()

        elif command == "fill":    # An option to fill the ingredients by an inputted amount
            water_fill = abs(int(input("Write how many ml of water do you want to add: \n")))
            milk_fill = abs(int(input("Write how many ml of milk do you want to add: \n")))
            bean_fill = abs(int(input("Write how many grams of coffee beans do you want to add: \n")))
            disp_fill = abs(int(input("Write how many disposable coffee cups do you want to add: \n")))
            CoffeeMachine.water_level += water_fill
            CoffeeMachine.milk_level += milk_fill
            CoffeeMachine.bean_level += bean_fill
            CoffeeMachine.disposable_cups += disp_fill
            self.ui()

        elif command == "take":    # An option to withdraw all the money stored and prints the amount taken
            print(f"I gave you ${CoffeeMachine.money}\n")
            CoffeeMachine.money = 0
            self.ui()

        else:
            print("That was not an option! Try again...\n")    # If an incorrect option is inputted by the user
            self.ui()


CoffeeMachine()    # Initializes the Class, in which the ui method is started
