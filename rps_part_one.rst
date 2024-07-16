Create Empty List
-------------------------------------------

.. code-block:: python
    
    game_details = []

Get User Name To Personalize the experience
-------------------------------------------

.. code-block:: python

    user_name = input("Welcome to Rock, Paper, Scissors! Please Enter Your Name: ").capitalize()

    game_details.append(user_name)


Get User Selection
--------------------

.. code-block:: python

    user_selection = input(f"Ok {user_name}, rock, paper or scissors? ").lower()

    game_details.append(user_selection)



Let's print User's Selections From List
---------------------------------------

.. code-block:: python

    print(f"Congratulations {game_details[0]}, you selected {game_details[1]}!")

    
