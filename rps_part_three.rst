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
