# Write your code here
class CoffeeMachine:
    def __init__(self, water, milk, coffeeBean, dispoCup, money):
        self.water = water
        self.milk = milk
        self.coffeeBean = coffeeBean
        self.dispoCup = dispoCup
        self.money = money

    def buy_espresso(self):
        if self.water < 250:
            print('Sorry, not enough water!')
        elif self.milk < 0:
            print('Sorry, not enough milk!')
        elif self.coffeeBean < 16:
            print('Sorry, not enough coffee!')
        elif self.dispoCup < 1:
            print('Sorry, not enough disposable cup!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.milk -= 0
            self.coffeeBean -= 16
            self.dispoCup -= 1
            self.money += 4

    def buy_latte(self):
        if self.water < 350:
            print('Sorry, not enough water!')
        elif self.milk < 75:
            print('Sorry, not enough milk!')
        elif self.coffeeBean < 20:
            print('Sorry, not enough coffee!')
        elif self.dispoCup < 1:
            print('Sorry, not enough disposable cup!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.coffeeBean -= 20
            self.dispoCup -= 1
            self.money += 7

    def buy_cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water!')
        elif self.milk < 100:
            print('Sorry, not enough milk!')
        elif self.coffeeBean < 12:
            print('Sorry, not enough coffee!')
        elif self.dispoCup < 1:
            print('Sorry, not enough disposable cup!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.coffeeBean -= 12
            self.dispoCup -= 1
            self.money += 6

    def fill(self, water_fill, milk_fill, coffeeBean_fill, dispoCup_fill):
        self.water += water_fill
        self.milk += milk_fill
        self.coffeeBean += coffeeBean_fill
        self.dispoCup += dispoCup_fill

    def take(self):
        print(f'I gave you {self.money}')
        self.money = 0

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffeeBean} of coffee beans')
        print(f'{self.dispoCup} of disposable cups')
        print(f'{self.money} of money')
        print()


coffeeMachine1 = CoffeeMachine(401, 540, 120, 9, 550)
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    a = input()
    if a == 'buy':
        while True:
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            choose = input()
            if choose == '1':
                coffeeMachine1.buy_cappuccino()
                break
            elif choose == '2':
                coffeeMachine1.buy_espresso()
                break
            elif choose == '3':
                coffeeMachine1.buy_latte()
                break
            elif choose == 'back':
                break
    elif a == 'fill':
        print()
        waterFill = int(input('Write how many ml of water do you want to add:'))
        milkFill = int(input('Write how many ml of milk do you want to add:'))
        coffeeBeanFill = int(input('Write how many grams of coffee beans do you want to add:'))
        dispoCupFill = int(input('Write how many disposable cups of coffee do you want to add:'))
        coffeeMachine1.fill(waterFill, milkFill, coffeeBeanFill, dispoCupFill)
    elif a == 'take':
        coffeeMachine1.take()
    elif a == 'remaining':
        coffeeMachine1.remaining()
    elif a == 'exit':
        break
