import random
import time

class GameBoy():

    def rock_paper_scissors(self):

        options = ["rock", "paper", "scissors"]
        user = ""

        cpu_pick = random.choice(options)

        while True:
            try:
                user = int(input("""Pick one:
                                1. Rock
                                2. Paper
                                3. Scissors """))
                
                if user in [1,2,3]:
                    break

                else:
                    print("Please only select option 1, 2 or 3")
                    print()

            except ValueError:
                print("Invalid option, please select a number.")
        
    
        
        # rock
        def check_rock(cpu_pick):

            # win result
            if cpu_pick == "scissors":
                print("--- CPU selected SCISSORS ---")
                return 1
            
            # lose result
            if cpu_pick == "paper":
                print("--- CPU selected PAPER---")
                return 2
            
            # draw result
            if cpu_pick == "rock":
                print("--- CPU selected ROCK---")
                return 0
            
          # paper
        def check_paper(cpu_pick):

            # win result
            if cpu_pick == "rock":
                print("--- CPU selected ROCK---")
                return 1
            
            # lose result
            if cpu_pick == "scissors":
                print("--- CPU selected SCISSORS ---")
                return 2
            
            # draw result
            if cpu_pick == "paper":
                print("--- CPU selected PAPER---")
                return 0
            
          # scissors
        def check_scissors(cpu_pick):

            # win result
            if cpu_pick == "paper":
                print("--- CPU selected PAPER---")
                return 1
            
            # lose result
            if cpu_pick == "rock":
                print("--- CPU selected ROCK---")
                return 2
            
            # draw result
            if cpu_pick == "scissors":
                print("--- CPU selected SCISSORS ---")
                return 0

        # user selects rock
        if user == 1:
            print("*** YOU chose ROCK ***")
            time.sleep(2)
            result = check_rock(cpu_pick=cpu_pick)
            time.sleep(2)

        # user selects paper
        if user == 2:
            print("*** YOU chose PAPER ***")
            time.sleep(2)
            result = check_paper(cpu_pick=cpu_pick)
            time.sleep(2)

        # user selects scissors
        if user == 3:
            print("*** YOU chose SCISSORS ***")
            time.sleep(2)
            result = check_scissors(cpu_pick=cpu_pick)
            time.sleep(2)

        # Game result
        if result == 1:
            print()
            print(" ``` You WIN!!! ``` ")

        if result == 2:
            print()
            print(" ``` You LOSE!! ``` ")

        if result == 0:
            print()
            print(" ``` It's a DRAW!!! ``` ")

num = 1
print(type(num))
my_game = GameBoy()

my_game.rock_paper_scissors()

