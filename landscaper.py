class Landscaper:
    def __init__(self):
        # Initialize the money and tool attributes for the Landscaper
        self.money = 0
        self.tool = "teeth"
        
    def cut_grass(self):
        # Increase money based on the current tool
        if self.tool == "teeth":
            self.money += 1
        elif self.tool == "scissors":
            self.money += 5
        elif self.tool == "push_lawnmower":
            self.money += 50
        elif self.tool == "battery_lawnmower":
            self.money += 100
        elif self.tool == "team":
            self.money += 250

    def buy_tool(self, tool_choice):
        # Define the tools and their corresponding prices
        tool_prices = {
            1: ("scissors", 5),
            2: ("push_lawnmower", 25),
            3: ("battery_lawnmower", 250),
            4: ("team", 500)
        }

        if tool_choice in tool_prices:
            tool_name, cost = tool_prices[tool_choice]
            # Check if the Landscaper has enough money
            if self.money >= cost:
                self.money -= cost
                self.tool = tool_name
                return f"You bought {tool_name}"
            return "Unable to buy tool."
        return "Invalid tool option."

    def has_won(self):
        # Check if the Landscaper has won the game (has the "team" tool and at least $1000)
        return self.tool == "team" and self.money >= 1000

# Create a Landscaper game instance
game = Landscaper()

# Tool options menu
tool_options = """
Available tools for purchase:
[1] Scissors - $5
[2] Push Lawnmower - $25
[3] Battery Lawnmower - $250
[4] Team - $500
"""

# Game loop
while True:
    user_input = int(input(f"""
                    You now have ${game.money}
                    What would you like to do?
                    [1] Cut Grass
                    [2] Buy Tool
                    [3] Check Status
                    [4] Quit the Game
                    """))

    if user_input == 1:
        game.cut_grass()
        print(f"You now have ${game.money}")
        
    elif user_input == 2:
        print(tool_options)
        tool_choice = int(input("Enter the number of the tool you want to buy: "))
        result = game.buy_tool(tool_choice)
        print(result)
            
    elif user_input == 3:
        print(f"Current money: ${game.money}")
        print(f"Current tool: {game.tool}")
        
    elif user_input == 4:
        print("You quit the game")
        break
    
    if game.has_won():
        print("Congratulations, you've won the game!")
        break