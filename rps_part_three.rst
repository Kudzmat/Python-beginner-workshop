Let's Make Game Keep Running
-----------------------------

.. code-block:: python

    # create game on variable
    game_on = True

    while game_on:
      pass

Let's create a function that will welcome the player
-----------------------------------------------------

.. code-block:: python

    # our constants
    CPU_OPTIONS = ['rock', 'paper', 'scissors']
    USER_OPTIONS = ['rock', 'paper', 'scissors']

    # global variable name
    name = ""

    def game_menu():
      
      # get name
      global name  # we need to call the global variable before using it
      name = input("Welcome to Rock, Paper, Scissors! Please Enter Your Name: ").capitalize()


    while game_on:
        game_menu()
        print(name)
        break


Let's create more options for the player
-------------------------------------

.. code-block:: python
  
    def game_menu():  
        # get name
        global name  # we need to call the global variable before using it
        name = input("Welcome to Rock, Paper, Scissors! Please Enter Your Name: ").capitalize()
        print()

        menu_selection = input("""
        Welcome {name}, what would you like to do?
        1. Play Game
        2. Exit Game
        """)
    
        return menu_selection  # why do we return and not print?


    while game_on:
        print(game_menu())  # check we are returning something
        break


Defensive programming for using numbers for options
---------------------------------------------------

.. code-block:: python

    logged = False
    # options = [1,2]

    while not logged:
        # type casing to make sure we get int
        menu_selection = int(input(f"""
                Welcome {name}, what would you like to do?
                1. Play Game
                2. Exit Game
                """))

        # many ways to create defence
        if menu_selection < 1 or menu_selection > 2: # if menu_selection not in options
            print("Please select either 1 or 2")
            logged = False
        else:
            logged = True

    return menu_selection


Let's create a function for playing the game
----------------------------------------------


.. code-block:: python

    # let students try this
    def play_game():

        # we want to play multiple rounds
        playing = True

        while playing:
            # type casting
            user_selection = int(input("""Please Select One:
            1. Rock
            2. Paper
            3. Scisoors"""))

            find_winner(user_selection)

        # user_selection as parameter
    def find_winner(user_selection):
        pass

    # let's also add the option to exit the game using exit()
    while game_on:
            menu_selection = game_menu()

            # play game
            if menu_selection == 1:
                pass
            # exit the game
            else:
                game_on = False
    
    exit()


Let's create even better game logic
----------------------------------------------


.. code-block:: python

    # constant for game rules using dictionary 
    GAME_RULES = {
    1: {'strong': 'scissors', 'weak': 'paper'},
    2: {'strong': 'rock', 'weak': 'scissors'},
    3: {'strong': 'paper', 'weak': 'rock'}
    }

    CPU_CHOICES = ["rock", "paper", "scissors"]

    def find_winner(user_selection):

        # use for loop to start game
        for item in CPU_CHOICES:
            print(f"{item.capitalize()}...")
            time.sleep(1)

        # get cpu option
        cpu = random.choice(CPU_CHOICES)

        # show each option
        # since we're using numbers, we can index with a list
        print(f"{name} - {CPU_CHOICES[user_selection - 1]} vs CPU - {cpu}")
        print("-------------------------------------")

        
        # win
        if GAME_RULES[user]['strong'] == cpu:
            return "*** You Win!!! ***", 1
        
        # lose
        elif GAME_RULES[user]['weak'] == cpu:
            return "--- You Lose! --- :(", 2
        
        # tie
        else:
            return "^^^ It's a Tie!! ^^^ ", 0


Game results and score logic
------------------------------


.. code-block:: python

    def play_game():

        # counters for keeping game score
        win = 0
        loss = 0
        draw = 0

        # we want to play multiple rounds
        playing = True

        while playing:
            # type casting
            user_selection = int(input("""Please Select One:
            1. Rock
            2. Paper
            3. Scisoors"""))

            # save results in a variable (will be a tuple)
            results = find_winner(user_selection)

        
            # game results
            # win
            if result[1] == 1:
                win += 1
            # loss
            elif result[1] == 2:
                loss += 1
            # draw
            else:
                draw += 1

            print(result[0])  # show game result
            # show current record
            print(f"""
            Current Record:
            Wins - {win} | Losses {loss} | Draws {draw}""")


Replaying game and exiting
------------------------------


.. code-block:: python

    def replay():
            
            menu_options = [1,2]
            confirmed = False # user has not selected option
            
            # play again or exit
            while not confirmed:
                option = int(input("""
                Please Select:
                1. Continue Playing
                2. Stop Playing and Exit"""))
    
                
                if option not in menu_options:
                    print("Please select either 1 or 2")
                    confirmed = False

                else:
                    confirmed = True
            return option

        # finish up play game logic
        def play_game():

            # counters for keeping game score
            win = 0
            loss = 0
            draw = 0
    
            # we want to play multiple rounds
            playing = True
    
            while playing:
                # type casting
                user_selection = int(input("""Please Select One:
                1. Rock
                2. Paper
                3. Scisoors"""))
    
                # save results in a variable (will be a tuple)
                results = find_winner(user_selection)
    
            
                # game results
                # win
                if result[1] == 1:
                    win += 1
                # loss
                elif result[1] == 2:
                    loss += 1
                # draw
                else:
                    draw += 1
    
                print(result[0])  # show game result
                # show current record
                print(f"""
                Current Record:
                Wins - {win} | Losses {loss} | Draws {draw}""")

                # run replay function
                replay_choice = replay()

                # restart from top of the while loop/ play again
                if option == 1:
                    continue
                else:
                    playing = False
        print(f"Bye {name}, thanks For Playing!")
        exit()


Bringing it all together!!
-----------------------------

.. code-block:: python

    # our constants
    CPU_OPTIONS = ['rock', 'paper', 'scissors']
    USER_OPTIONS = ['rock', 'paper', 'scissors']
    GAME_RULES = {
    1: {'strong': 'scissors', 'weak': 'paper'},
    2: {'strong': 'rock', 'weak': 'scissors'},
    3: {'strong': 'paper', 'weak': 'rock'}
    }

    # game menu
    def game_menu():  
        logged = False
        options = [1,2]
    
        while not logged:
            # type casing to make sure we get int
            menu_selection = int(input(f"""
                    Welcome {name}, what would you like to do?
                    1. Play Game
                    2. Exit Game
                    """))
    
            # many ways to create defence
            if menu_selection not in options:
                print("Please select either 1 or 2")
                logged = False
            else:
                logged = True
        return menu_selection

    def find_winner(user_selection):

        # use for loop to start game
        for item in CPU_CHOICES:
            print(f"{item.capitalize()}...")
            time.sleep(1)

        # get cpu option
        cpu = random.choice(CPU_CHOICES)

        # show each option
        # since we're using numbers, we can index with a list
        print(f"{name} - {CPU_CHOICES[user_selection - 1]} vs CPU - {cpu}")
        print("-------------------------------------")

        
        # win
        if GAME_RULES[user]['strong'] == cpu:
            return "*** You Win!!! ***", 1
        
        # lose
        elif GAME_RULES[user]['weak'] == cpu:
            return "--- You Lose! --- :(", 2
        
        # tie
        else:
            return "^^^ It's a Tie!! ^^^ ", 0

        def replay():
            
            menu_options = [1,2]
            confirmed = False # user has not selected option
            
            # play again or exit
            while not confirmed:
                option = int(input("""
                Please Select:
                1. Continue Playing
                2. Stop Playing and Exit"""))
    
                
                if option not in menu_options:
                    print("Please select either 1 or 2")
                    confirmed = False

                else:
                    confirmed = True
            return option

        def play_game():

            # counters for keeping game score
            win = 0
            loss = 0
            draw = 0
    
            # we want to play multiple rounds
            playing = True
    
            while playing:
                # type casting
                user_selection = int(input("""Please Select One:
                1. Rock
                2. Paper
                3. Scisoors"""))
    
                # save results in a variable (will be a tuple)
                results = find_winner(user_selection)
    
            
                # game results
                # win
                if result[1] == 1:
                    win += 1
                # loss
                elif result[1] == 2:
                    loss += 1
                # draw
                else:
                    draw += 1
    
                print(result[0])  # show game result
                # show current record
                print(f"""
                Current Record:
                Wins - {win} | Losses {loss} | Draws {draw}""")

                # run replay function
                replay_choice = replay()

                # restart from top of the while loop/ play again
                if option == 1:
                    continue
                else:
                    playing = False
        print(f"Bye {name}, thanks For Playing!")
        exit()

    game_on = True

    while game_on:
      game_option = game_menu()

        # play game
        if game_option == 1:
            play_game()
        # stop playing
        else:
            print(f"Bye {name}, thanks For Playing!")
            game_on = False
        
    exit()

