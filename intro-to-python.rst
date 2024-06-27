Getting started with Python
===========================

The Python interpreter
----------------------

Type ``python`` or ``python3`` in a terminal window::

    $ python3
    Python 3.7.3 (default, Jun 19 2019, 07:38:49)
    [Clang 10.0.1 (clang-1001.0.46.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

As long as the response starts with "Python 3...", that's OK. If you don't get it
by typing ``python`` try doing ``python3`` instead.

You're now in the Python interpreter. To exit, hit ``control d``.

In the interpreter, you type commands and press return::

    >>> 2 + 2
    4
    >>> 23 * 4.3
    98.89999999999999
    >>> hello computer
      File "<stdin>", line 1
        hello computer
                     ^
    SyntaxError: invalid syntax
    >>>


Simple maths
------------

We're using Python *operators*.

.. code-block:: python

    # addition

    print(6+7)

    # subtraction
    
    print(8-5)

    # multiplication
    
    print(2*3)

    # division
    
    print(3/2)
    

Some other useful *operators*

.. code-block:: python

    # 3 to the power of 2
    
    print(3 ** 2)
    
    # is division, returns whole numbers
    
    print(19//4) 
    
    # mod operator returns the remainder 
    
    print(19%4)
    


https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

Numbers Quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/numbers.rst 


Variables Assignments
---------

.. code-block:: python

    # number of siblings
    my_siblings = 3

    # number of puppies
    puppies = 27

    # result
    print(puppies / my_siblings)

    # further calculations
    # how many puppies each sibling gets
    allocated_puppies = puppies / my_siblings
    print(allocated_puppies)

    # you can also reassign variables
    puppies = 30
    print(puppies)

    # in Python you can reassign to different data type
    puppies = ["Shaq", "Lonzo", "Jerry"]
    print(puppies)

    # check variable type
    type(puppies)


Strings
-------

.. code-block:: python

    # double quotes
    print("hello")

    # single quotes
    print('world')

    # sentences are also strings
    # white spaces also count as characters
    print("I am also a string')

    # errors
    print('Hey, I'm feeling good')

    # checking the length of a string
    len("hello")

    mood = 'I am happy!'
    len(mood)

    # indexing and slicing
    my_string = "Hello World"

    # return first character
    print(my_string[0])

    # return r
    print(my_string[8]

    # return l
    print(my_string[9])
    print(my_string[-3])

    # slicing
    my_string = "abcdefghijk"

    # start from c until the end
    print(my_string[2:]

    # from a up to but not including d
    print(my_string[:3]

    # grab def
    print(my_string[3:6]

    # step size of two
    print(my_string[::2])

    print(my_string[2:7:2]

    # trick to reverse your string
    # beginning to end in steps of -1
    print(my_string[::-1])


String properties and methods
------------------------------

.. code-block:: python

    # immutability

    # you want to change name from "Sam" to "Pam"
    name = "Sam"    

    # this won't work
    name[0] = 'P'

    # Creating a new string 
    last_letters = name[1:]
    name = "p" + last_letters
    print(new_name)

    # new sentence
    x = "Hello world"
    x = x + "it is beautiful outside"
    print(x)

    # make sure you don't use wrong data type
    2 + 3
    '2' + '3'

    # built-in methods
    name = "kudzayi"

    # upper case
    name.upper()

    # if you want it to change you need to reassign
    # name = name.upper()

    # lowercase
    name.lower()

    # uppercase first letter
    name.capitalize()

Strings Quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/strings.rst 


Lists
-------

.. code-block:: python

    # same data type
    my_list = [1,2,3]

    # various data types
    my_list = [1, "hello", 3.5, 10]

    # check length
    len(my_list)

    # indexing
    my_list[1]
    my_list[1:3]

    # concatnation 
    another_list = ["Tom", "Jerry"]
    new_list = my_list + another_list

    # lists are mutable
    new_list[0] = "Scooby"

    # adding element to end of list with built-in methods
    new_list.append("Buggs")

    # remove item at the end, it is returned
    popped_element = new_list.pop()
    print(popped_element)

    # removing at a specific index
    popped_index = new_list.pop(2)

    # sorting a list
    new_list = ['x', 'h', 'c', 'b', 'e', 'a', 'f']
    num_list = [8, 9, 1, 4, 3, 5]

    # does not create new list, sorts current list
    new_list.sort()
    num_list.sort()

    # reversing a list
    new_list.reverse()
    num_list.reverse()


http://docs.python.org/3/tutorial/introduction.html#lists
Lists quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/lists.rst

Comparisons, and True and False
-------------------------------

Python *comparison operators*

::

    >>> # are they equal?
    >>> 1 == 2
    False
    >>> 1 == 1
    True
    >>> a = 10
    >>> b = 10
    >>> a == b
    True
    # are they not equal?
    >>> 1 != 2
    True
    # greater and less than
    >>> 2 > 1
    True
    >>> 1 < 2
    True
    # also <= and >=


Tuples, lists and sets
----------------------

Tuples, lists and sets are all examples of Python *collections*.


Tuples
^^^^^^

::

    >>> elements = ("hydrogen", "helium", "lithium", "beryllium", "boron")
    >>> type(elements)
    <type 'tuple'>

    # slicing a tuple
    >>> elements[0]
    'hydrogen'
    >>> elements[3]
    'beryllium'
    >>> elements[1:4]
    ('helium', 'lithium', 'beryllium')
    >>> elements[-1]
    'boron'


Sets
^^^^

A set is an unordered collection with no duplicate elements.

::

    >>> life = ["fun", "fun", "fun", "boring", "fun"]
    >>> set(life)
    set(['fun', 'boring'])


Dictionaries
------------

::

    >>> legs = {"spider": 6, "dog": 4, "bird": 2, "ant": 6}
    >>> legs["bird"]
    2

    # we don't have humans
    >>> legs["human"]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'human'
    >>>

    # a safer way if we're not sure if the key's present
    >>> legs.get("human")
    # or even
    >>> legs.get("human", "no data available")

    # better add human though anyway
    >>> legs["human"] = 2

    # and we'd better correct the entry for spiders
    >>> legs["spider"] = 8


https://docs.python.org/3/tutorial/datastructures.html#dictionaries


Loops
-----

::

    >>> for item in range(100):
    ...     item
    ...
    0
    1
    [etc]for item in elements

    >>> for element in elements:
    ...     element
    ...
    'beryllium'
    'boron'
    'helium'
    'hydrogen'
    'lithium'
    37
    ['pancakes', 'bread']


    # list comprehensions are an excellent way to build lists
    >>> squares = [item * item for item in range(10)]
    >>> squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # you can add an if clause to filter the results
    # let's get squares of even numbers only
    >>> squares = [item * item for item in range(10) if item % 2 == 0]
    >>> squares
    [0, 4, 16, 36, 64]


Functions
---------

::

    >>> def squares():
    ...     return [item * item for item in range(10)]
    ...
    >>> squares()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

This function only does one thing, so it's not that useful. So::

    # define squares() with a required argument
    >>> def squares(up_to):
    ...     return [item * item for item in range(up_to)]
    ...
    >>> squares()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: squares() takes exactly 1 argument (0 given)

    # we have to provide the argument
    >>> squares(15)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]

    # or we could have defined it with a default argument of 10
    >>> def squares(up_to=10):
    ...     return [item * item for item in range(up_to)]
    ...

We can have multiple arguments::

    >>> def multiples(up_to=10, multiply_by=2):
    ...     return [item * multiply_by for item in range(up_to)]
    ...
    >>> multiples()
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> multiples(10, 5)
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

    # using named arguments when calling a function allows you to use
    # them in a different order
    >>> multiples(multiply_by=10, up_to=5)
    [0, 10, 20, 30, 40]


Let's play a game. For this we need to *import* the ``random`` *module*, and
use the ``choice()`` function.

::

    >>> import random


``choice()`` takes an argument, which needs to be a sequence of some sort, and
chooses between them at random::

    >>> random.choice(("black", "white", "red"))

    # strings are sequences too!
    >>> random.choice("Refer to the documentation for details")

::

    >>> def challenge(player_choice=None):
    ...     if player_choice is None:
    ...         print("you have to choose something!")
    ...     elif player_choice is random.choice([True, False]):
    ...         print("You win!")
    ...     else:
    ...         print("You lose!")
    ...

It's not a very interesting::

    >>> challenge()
    you have to choose something!
    >>> challenge(True)
    You win!
    >>> challenge(True)
    You lose!
    >>> challenge(True)
    You lose!

Let's make the computer play the game against itself::

    >>> for r in range(1000):
    ...     challenge(random.choice([True, False]))


Scripts
-------

Put all this in a file called game.py::

    import random

    # define the challenge function
    def challenge(player_choice=None):
        if player_choice is None:
            print("You have to choose something!")
        elif player_choice is random.choice([True, False]):
            print("You win!")
        else:
            print("You lose!")

    for r in range(1000):
        challenge(random.choice([True, False]))

Exit the Python interpreter (``control d``) and run the command::

    python3 game.py

This tells Python to run the script - the program - ``game.py``.

Classes
-------

Things in Python are instances of classes. Some are already defined, with their
own *methods* (methods are functions that belong to a class), such as lists and
dictionaries and so on, but you can also create your own.

::

    >>> class Animal(object):
    ...     def identify(self):
    ...         print("I am an animal")
    ...
    >>> dog = Animal()
    >>> dog.identify()
    I am an animal
    >>> cat = Animal()
    >>> cat.identify()
    I am an animal

We can make this a little more interesting::

    >>> class Animal(object):
    ...     def __init__(self, noise=None):
    ...         self.noise = noise
    ...     def identify(self):
    ...         print("I am an animal, and I go", self.noise)
    ...

    # create an Animal instance, and provide the string "woof" to its
    # initialiser
    >>> dog = Animal("woof")
    >>> dog.identify()
    I am an animal, and I go woof

    # we can modify an object's attribute once it has been created
    >>> dog.noise = "bow wow"
    >>> dog.identify()
    I am an animal, and I go bow wow
