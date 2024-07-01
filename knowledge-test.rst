Strings
----------

Given the string 'hello' give an index command that returns 'e'.

.. code block:: python

    s = 'hello'
    # Print out 'e' using indexing

Reverse the string 'hello' using slicing:

.. code block:: python

    s ='hello'
    # Reverse the string using slicing

Given the string hello, give two methods of producing the letter 'o' using indexing.

.. code block:: python

    s ='hello'
    # Print out the 'o' using two different indexing methods


Lists
-------

Build this list [0,0,0] two separate ways.

Reassign 'hello' in this nested list to say 'goodbye' instead:

.. code block:: python

    list3 = [1,2,[3,4,'hello']]

Sort the list below:

.. code block:: python

    list4 = [5,3,4,6,1]


Dictionaries
------------

Using keys and indexing, grab the 'hello' from the following dictionaries:

.. code block:: python

    d = {'simple_key':'hello'}
    # Grab 'hello'

    d = {'k1':{'k2':'hello'}}
    # Grab 'hello'

    # Getting a little tricker
    d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
    #Grab hello

    # This will be hard and annoying!
    d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

Can you sort a dictionary? Why or why not?


Tuples
--------

What is the major difference between tuples and lists?

How do you create a tuple?


Sets
--------

What is unique about a set?

Use a set to find the unique values of the list below:

.. code block:: python

    list5 = [1,2,2,33,4,4,11,22,3,3,2]


Booleans
--------

What will be the resulting Boolean of the following pieces of code

.. code block:: python

    2 > 3

    3 <= 2

    3 == 2.0

    3.0 == 3

    4**0.5 != 2

Final Question: What is the boolean output of the cell block below?

.. code block:: python

    # two nested lists
    l_one = [1,2,[3,4]]
    l_two = [1,2,{'k1':4}]

    # True or False?
    l_one[2][0] >= l_two[2]['k1']
