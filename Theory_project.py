class VendingMachine:

    def __init__(self):
        self.state = 'A'  # Initial state A (0 JD)
        self.state_values = {
            'A': 0.0,  
            'B': 0.25,  
            'C': 0.50,  
            'D': 0.75,  
            'E': 1.0    
        }

    def insert_coin(self, coin):
        if coin not in [0.25, 0.50]:
            print(" Invalid input!! Please only insert 0.25 JD or 0.50 JD.")
            return

        print(f"\n Inserting {coin} JD")
        print(f" Current state: {self.state} (Total: {self.state_values[self.state]} JD)")

        if self.state == 'A':
            if coin == 0.25:
                self.state = 'B'
            elif coin == 0.50:
                self.state = 'C'

        elif self.state == 'B':
            if coin == 0.25:
                self.state = 'C'  
            elif coin == 0.50:
                self.state = 'D'   

        elif self.state == 'C':
            if coin == 0.25:
                self.state = 'D'   
            elif coin == 0.50:
                self.state = 'E'   

        elif self.state == 'D':
            if coin == 0.25:
                self.state = 'E'  
            elif coin == 0.50:
                self.state = 'E'  

        elif self.state == 'E':  # or just go back to state A (reset)
            if coin == 0.25:
                self.state = 'B'   
            elif coin == 0.50:
                self.state = 'C'  

        print(f" New state: {self.state} (Total: {self.state_values[self.state]} JD)")

        if self.state == 'E':
            self.dispense_product()

    def dispense_product(self):
        print("\n >>>> PRODUCT DISPENSED! <<<<")
        print(f" Total paid: {self.state_values[self.state]} JD")
        print(" Thank you for your purchase!")

    def get_status(self):
        print("\n >>>> Current Status:")
        print(f"   State: {self.state}")
        print(f"   Amount paid: {self.state_values[self.state]} JD")
        remaining = 1.0 - self.state_values[self.state]
        print(f"   Amount needed to reach 1 JD: {remaining} JD")

def main():

    print("\n >>>> VENDING MACHINE <<<<")
    print(" Product cost: 1.00 JD")
    print(" Accepted coins: 0.25 JD, 0.50 JD")

    vm = VendingMachine()

    while True:
        vm.get_status()
        user_input = input("\n Insert coin (0.25/0.50) or 'E' to exit: ").strip()

        if user_input.lower() == 'e':
            print("\n Thank you for using the vending machine!!")
            break

        try:
            coin = float(user_input)
            vm.insert_coin(coin)

        except ValueError:
            print(" Invalid input! Please enter 0.25, 0.50, or 'E'.")

if __name__ == "__main__":
    main()
