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
    
