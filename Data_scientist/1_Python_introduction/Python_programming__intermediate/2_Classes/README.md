Data Scientist / Python Introduction / Python Programming: Intermediate / Classes
=================================================================================

1. NFL Data
-----------

Recap of the dataset

Year | Week | Winner | Loser
:---:|:---:|:---:|:---:|
'2009' | '1' | 'Pittsburgh Steelers' | 'Tennessee Titans'
'2009' | '1' | 'Minnesota Vikings' | 'Cleveland Browns'
'2009' | '1' | 'New York Giants' | 'Washington Redskins'

2. Introduction to objects and classes
--------------------------------------

Class - template of entities to be represented, e.g. car

Object - instance of a class which actually represents an entity, e.g. Black honda accord

3. Class syntax
---------------

`__init__()` method of a `class` contains definitions of properties.

```python
class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"
```

4. Instance methods and \_\_init\_\_
------------------------------------

`__init__()` can have its own parameters which can be used to initialize objects.

```python
class Team():
    def __init__(self, name):
        self.name = name

bucs = Team("Tampa Bay Buccaneers")
```

5. The `self` keyword
---------------------

Actually `self` is not a real keyword in Python, it is just the first argument passed to `__init()__`.
It's used to point to the object itself. The methods which include `self` (or whatever the name of the pointing variable is),
those methods become **instance methods**. 

6. More instance methods
------------------------

`print_name()` and `count_total_wins()` methods are added which will print the name and count total wins of _that instance_.

```python
# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        
    # Your method goes here
    def count_total_wins(self):
        wins = 0
        for game in nfl:
            if game[winner_column] == self.name:
                wins += 1
        return wins
```

7. Adding to the `__init__()` function
--------------------------------------

Abstract away the `nfl` variable and add it to the class definition by including it into `__init__()` method.

8. Wins in a year
-----------------

Same as above. 
