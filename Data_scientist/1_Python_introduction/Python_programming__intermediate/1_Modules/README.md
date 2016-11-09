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

