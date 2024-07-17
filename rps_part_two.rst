Get CPU Selection Using Random Library
--------------------------------------

.. code-block:: python

    import random

    cpu_options = ['rock', 'paper', 'scissors']

    cpu_choice = random.choice(cpu_options)

    print(cpu_choice)


Combine With the Previous Code
----------------------------

.. code-block:: python

    # get name
    user_name = input("Welcome to Rock, Paper, Scissors! Please Enter Your Name: ").capitalize()

    # get choice
    user_selection = input(f"Ok {user_name}, rock, paper or scissors? ")

    print(f"{user_name} selected: {user_selection} \nCPU selected: {cpu_choice}")


Pick the Winner with if statements
-----------------------------------

.. code-block:: python

    # draw
    if user_selection == cpu_choice:
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** It's a tie! ***")

    # rock options
    elif user_selection == 'rock' and cpu_selection == 'paper':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Lose :( ***")

    elif user_selection == 'rock' and cpu_selection == 'scissors':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Win!!! :D ***")

    # paper options
    elif user_selection == 'paper' and cpu_selection == 'rock':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Lose :( ***")

    elif user_selection == 'paper' and cpu_selection == 'scissors':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Win!!! :D ***")

    # scissors options
    elif user_selection == 'scissors' and cpu_selection == 'rock':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Lose :( ***")

    elif user_selection == 'scissors' and cpu_selection == 'paper':
        print(f"{user_name}: *{user_selection}* VS CPU: *{cpu_choice}*")
        print("*** You Win!!! :D ***")

    else:
        print("Hmmmm, something's not right..... Try again")


Add Defensive Programming / Error Handling
-------------------------------------------

.. code-block:: python

    user_options = ['rock', 'paper', 'scissors']

    # get choice
    user_selection = input(f"Ok {user_name}, rock, paper or scissors? ").lower()  # standardize responses

    if user_selection not in user_options:
        print("Please only select 'rock paper or scissors!'")
        exit()

    
    
    
