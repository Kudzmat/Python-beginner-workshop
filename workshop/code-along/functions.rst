Functions #1
-------

Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

lesser_of_two_evens(2,4) # should return --> 2
lesser_of_two_evens(2,5) # should return --> 5

.. code-block:: python

    def lesser_of_two_evens(a,b):
        pass

    # Check
    lesser_of_two_evens(2,4)
    # Check
    lesser_of_two_evens(2,5)

Functions #2
-------

Write a function takes a two-word string and returns True if both words begin with same letter.

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

.. code-block:: python

    def animal_crackers(text):
        pass

    # Check
    animal_crackers('Levelheaded Llama')
    # Check
    animal_crackers('Crazy Kangaroo')


Functions #3
-------

Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False.

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False

.. code-block:: python

    def makes_twenty(n1,n2):
        pass

    # Check
    makes_twenty(20,10)
    # Check
    makes_twenty(2,3)


Functions #
-------

Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'

.. code-block:: python

    def old_macdonald(name):
        pass

    # Check
    old_macdonald('macdonald')


Functions #5
-------

Given a sentence, return a sentence with the words reversed

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"

.. code-block:: python

    def master_yoda(text):
        pass


    # Check
    master_yoda('I am home')
    # Check
    master_yoda('We are ready')



CHALLENGING PROBLEM
--------------------

Write a function that takes in a list of integers and returns True if it contains 007 in order.

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False


For Example:

.. code-block:: python

   def spy_game(nums):
    pass


    # Check
    spy_game([1,2,4,0,0,7,5])
    # Check
    spy_game([1,0,2,4,0,5,7])
    # Check
    spy_game([1,7,2,0,4,5,0])
