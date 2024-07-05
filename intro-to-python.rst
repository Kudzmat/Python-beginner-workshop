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

    # printitng variables
    my_car = "Tesla"
    print(my_car)

    # new car
    new_car = input("What car do you have now?" )

    print(new_car)

    # printitng in a sentence
    print("My car is a " + new_car)
    print("My car is a ", new_car)
    print(f"My car is a {new_car}")

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

Dictionaries
------------

.. code-block:: python

    menu = {"hamburger": 3, "chicken": 2, "fries": "1"}
    print(menu["chicken"])

    # lists in a dictionary
    menu = {"hamburger": 3, "chicken": 2, "fries": "1", "drinks": ['wine', 'beer', 'soft drinks']}

    print(menu["drinks"])

    # stacking calls
    drinks_menu = menu["drinks"]

    # beer
    drink_type = drinks_menu[1]

    # capitalize beer
    drink_type.capitalize()

    # you can do this in one move
    menu["drinks"][0].capitalize()

    # adding new items
    menu['ribs'] = 200
    print(menu)

    # changing 
    menu['ribs'] = 5.99
    print(menu)

    # grabbing all keys
    menu.keys()

    # values
    menu.values()

    # key, value pairs
    menu.items()  # returns tuple

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Dictionaries quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/dictionaries.rst


Tuples
-------

.. code-block:: python

    t = (17,9,93)
    my_list = [17,9,93]
    
    type(t)
    type(my_list)
    
    # slicing & indexing
    t[0]
    t[-1]

    # count
    t = ('a', 'a', 'c')
    print(t.count('a'))

    # returns from instance 
    print(t.index('a'))

    # differences
    my_list[0] = 'New'
    # does not have the flexibility of a list
    # provides data integrity as you will not accidentally change data in large peieces of code
    t[0] = 'New' 

Tuples quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/tuples.rst 


Sets
------------

.. code-block:: python

    my_set = set()
    
    my_set.add(1)
    
    print(my_set)
    
    my_set.add(2)
    
    print(my_set)
    
    my_set.add(2)
    
    print(my_set)
    
    # useful to cast a list as a set
    my_list = [1,1,2,3,3,3,3,3,4,5]
    
    set(my_list)
    
    print(my_list)

Sets quiz ---> https://github.com/Kudzmat/Python-Installation-Tutorial/blob/main/sets.rst 


Booleans and Comparisons
-------------------------

.. code-block:: python

    # are they equal?
    1 == 2
    
    1 == 1
    
    a = 10
    
    b = 10
    
    a == b
    
    # are they not equal?
    1 != 2
    
    # greater and less than
    2 > 1
    
    1 < 2
    # also <= and >=


Python Statements if/elif/else
-------------------------------

.. code-block:: python

    # true statement
    if 3 > 2:
        print("It's True!")

    # using variables
    hungry = False
    if hungry:
        print("I'm STARVING!!")
    # add else
    else:
        print("I'm not hungry!!!")


    # multiple scenarios
    language = "python"

    if language == 'python':
        print("Python Rocks!!!")
    elif language == 'java':
        print("I prefer coffee")
    elif language == 'swift':
        print("Apple products are cool")
    else:
        print("I'm not familiar with this programming language")

 

For Loops
---------

.. code-block:: python

    my_list = [1,2,3,4,5,6,7,8,9,10]

    # create a for loop to iterate over item
    for num in my_list:
        print(num)

    # printing hello 10 times
    for num in my_list:
        print("hello")

    # check for even numbers by combining with control flow
    for num in my_list:
        if num % 2 == 0:
            print(num)
        else:
            print("This is an odd number")

    # get sum of all numbers
    list_sum = 0
    for num in my_list:
        list_sum = list_sum + num
        print(list_sum)
    # printing outside for loop prints final value

    # looping through strings
    my_string = "Hello World"
    for letter in my_string:
        print(letter)

    # you can also use an _
    for _ in my_string:
        print("cool")

    # tuple unpacking
    my_list = [(1,2),(3,4),(5,6),(7,8)]

    # printing a's
    for a,b in my_list:
        print(a)

    my_list = [(1,2,3),(4,5,6)]
    # printing c's
    for a,b,c in my_list:
        print(c)

    # unpacking dictionaries
    d = {'k1':1,'k2':2,'k3':3}

    # will iterate through keys by default
    for item in d:
        print(item)

    # iterate through items
    for item in d.items():
        print(item)    

    # you just want the values
    for key,value in d.items():
        print(value)

    for value in d.values():
        print(value)

While Loops
------------

.. code-block:: python

    x = 0 
    while x < 5:
        print(f"The current value of x is {x}")
        # x = x + 1
        x += 1
    else:
        print("X is not less than 5")

    # using pass
    x = [1,2,3]
    for item in x:
        # leaving empty will cause an error because Python is expecting something
        pass  # do nothing

    # continue
    my_string = "Sammy"
    for letter in my_string:
        if letter == 'a':
            continue  # go back to the top & continue the loop
        print(letter)

    # break when x = 2
    x = 5
    while x < 5:
        if x == 2:
            break
        print(x)
        x +=1



Functions
---------

.. code-block:: python

    # no need to repeat code
    def say_hello():
        print("hello")
        print("how")
        print("are")
        print("you")

    say_hello()

    # with parameters
    def say_hello(name):
        print(f"hello {name}")

    say_hello("Snoopy")

    # setting default parameter
    def say_hello(name="Adam"):
        print(f"hello {name}")

    # using return
    def add_num(num1, num2):
        return num1 + num2

    result = add_num(10,20)

    # functions with logic
    2 % 2 # remainder after division is 0 so even num
    41 % 40 # remainder after division is 1 so odd num

    def even_check(num):
        return num % 2 == 0

    even_check(20)  # True
    even_check(35)  # False

    # return true if any num in list is even
    
    def check_even_list(num_list):
        for num in num_list:
            if num % 2 == 0:
                return True  # functions end after return statement is executed
            else:
                pass # don't do anything

        return False  # if loop has completed without returning True, return False


    # return all the even numbers
    def check_even_list(num_list):

        # common to have placeholder variables at the top of function
        even_numbers = []

        for num in num_list:
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                pass # don't do anything

        return even_numbers


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
