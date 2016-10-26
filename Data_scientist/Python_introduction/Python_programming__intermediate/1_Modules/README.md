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

```python
winner_column = 2
for game in nfl:
    if game[winner_column] == "New England Patriots":
        patriots_wins += 1
```
