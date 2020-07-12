class CoffeMachine:
    preparation_materials = ["water", "milk", "coffe beans", "disposable cups", "money"]
    material_quantities = [400, 540, 120, 9, 550]
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    def status_checker(self):
        for index in range(4):
            print(self.material_quantities[index], "of", self.preparation_materials[index])
        print("$", str(self.material_quantities[4]), "of", self.preparation_materials[4])

    def buy_base(self, ctype):
        for z in range(4):
            if self.material_quantities[z] < ctype[z]:
                print("Sorry, not enough", self.preparation_materials[z], "!")
                return
        print("I have enough resources, making you a coffe!")
        for a in range(4):
            self.material_quantities[a] -= ctype[a]
        self.material_quantities[4] += ctype[4]

    def buy(self):
        coffe_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if coffe_type == "1":
            self.buy_base(self.espresso)
        elif coffe_type == "2":
            self.buy_base(self.latte)
        elif coffe_type == "3":
            self.buy_base(self.cappuccino)
        else:
            return

    def fill(self):
        for x in range(2):
            print("How many ml of", self.preparation_materials[x], "do you want to add")
            self.material_quantities[x] += int(input())
        self.material_quantities[2] += int(input("Write how many grams of coffee beans do you want to add:\n "))
        self.material_quantities[3] += int(input("Write how many disposable cups of coffee do you want to add:\n "))

    def take(self):

        print("I gave you", str(self.material_quantities[4]))
        self.material_quantities[4] = 0

    def main(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n ")
            print()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status_checker()
            else:
                break


machine = CoffeMachine()
machine.main()