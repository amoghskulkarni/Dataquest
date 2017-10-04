Data Scientist / Python Introduction / Python Programming: Intermediate / Modules
=================================================================================

1. NFL Data
-----------

Dataset (first 3 rows) looks like -

Year | Week | Winner | Loser
:---:|:---:|:---:|:---:|
'2009' | '1' | 'Pittsburgh Steelers' | 'Tennessee Titans'
'2009' | '1' | 'Minnesota Vikings' | 'Cleveland Browns'
'2009' | '1' | 'New York Giants' | 'Washington Redskins'

2. Modules
----------

**Module** is a collection of functions, variables and classes that have been bundled together in one file.
You can import a module by using `import`. Once imported, they are stored as a module object under the hood,
and the stuff inside it can be accessed by dot notation like follows - 

```python
import math
print(math.sqrt(4.0))       # 2.00
```

**Namespace** is a dictionary that contains all of the names we can refer to in our code. When we import a module this way, we add all of the objects and functions within that module to the global namespace. Before running our code, the Python interpreter adds all of the objects and functions that are available by default (`print()`, `list()`, etc.) to the global namespace.

Some modules have long names, however, and this means that we need to use the full module name each time we want to use any of the objects within that module. Instead, we can assign an alias when we import the module -

```python
import my_module as m
m.function1()
```

You can avoid typing the name of the module again and again by importing specific contents of the module in the namespace directly. That way you don't have to type `.` along with the name of the module.

```python
from math import function1
from math import function1, function2
```

Or you can add everything in the module by using `*`, but it is not a good practice. Avoid **polluting namespace** by adding specific contents of the module.

3. The `math` module
--------------------

`math.sqrt()` for square root.
`math.ceil()` for ceiling a float.
`math.floor()` for flooring a float.

4. Variables in modules
-----------------------

Some modules export variables which are stored in those modules. For example -

```python
import math
print(math.pi)              # Prints value of pi
```

5. The `csv` module
-------------------

`csv.reader()` returns an object which represents the data in our `csv` file. The function accepts file
object as an argument. The data has to be converted into a list (?). 

```python
f = open("nfl.csv")
nfl = list(csv.reader(f))
```

6. Counting how many times a team won
-------------------------------------

`nfl` contains csv data in the form of a list, `patriots_wins` is the counter.

```python
winner_column = 2
for game in nfl:
    if game[winner_column] == "New England Patriots":
        patriots_wins += 1
```

7. Making a function to count wins
----------------------------------

A function which has the above code in its body, and accepts the name of the team as an argument.

8. A brief note about booleans
------------------------------

`and` and `or` operators. And their truth tables. Zz.

9. The `or` keyword
-------------------

Zzz.

10. Working with boolean operators
----------------------------------

Examples for `and` and `or`.

11. Counting wins in a given year
---------------------------------

Check the given year and the given team in the row for gathering the datapoints. Use `and`.

```python
year_column = 0
winner_column = 2
def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[0] == year and row[2] == team:
            count = count + 1
    return count
```

12. Sharing modules
-------------------

