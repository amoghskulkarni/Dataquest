Data Scientist / Python Introduction / Python Programming: Intermediate / List comprehensions
=============================================================================================

1. The dataset
--------------

Legislators dataset at the end of the last example -

last\_name | first\_name | birthday | gender | type | state | party | birth\_year
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
'Bassett' | 'Richard' | '1745-04-02' | 'M' | 'sen' | 'DE' | 'Anti-Administration' | 1745
'Bland' | 'Theodorick' | '1742-03-21' | | 'rep' | 'VA' | | 1742
'Burke' | 'Aedanus' | '1743-06-16' | | 'rep' | 'SC' | | 1743
'Carroll' | 'Daniel' | '1730-07-22' | 'M' | 'rep' | 'MD' | | 1730

`csv` format -

```python
last_name,first_name,birthday,gender,type,state,party,birth_year
Bassett,Richard,1745-04-02,M,sen,DE,Anti-Administration,1745
Bland,Theodorick,1742-03-21,M,rep,VA,1742
Burke,Aedanus,1743-06-16,M,rep,SC,1743
Carroll,Daniel,1730-07-22,M,rep,MD,1730
```

2. Enumerate
------------

While iterating through a list in Python, if you want to access the index in the list - use `enumerate()`, which is a built-in
function which returns a list of tuples that include the index and the element for every element of the list.

```python
enumerate([10, 20, 30])         # Will create an iterable object which after iterating over it will give - (0, 10), (1, 20) and (2, 30)
```

Example -

```python
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])
```

3. Adding columns
-----------------

We can use `enumerate()` to add column to list-of-lists kind of data structure.

```python
door_count = [4, 4]
cars = [
        ["black", "honda", "accord"],
        ["red", "toyota", "corolla"]
       ]

for i, car in enumerate(cars):
    car.append(door_count[i])
```

4. List comprehensions
----------------------

A syntactic sugar for writing simple `for` loops written to iterate on the list.

Example - 

```python
animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]

animal_lengths = []
for animal in animals:
    animal_lengths.append(len(animal))
```

The above code can be written in a single line with list comprehension as following -

```python
animal_lengths = [len(animal) for animal in animals]
```

5. Counting up female names
---------------------------

Goal is to count female legislators' names' occurance in the dataset after 1940.

```python
name_counts = {}
gender_column = 3
year_column = 7
first_name_column = 1

for legislator in legislators:
    if legislator[gender_column] == 'F' and legislator[year_column] > 1940:
        name = legislator[first_name_column]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
```

6. `None`
---------

`None` is a special kind of object (of type `NoneType`) that are there to show the variable has no value.

While comparing a variable with `None` - instead of using `==`, `variable is None` syntax is used.

The `is` comparison operator checks for object equality. Using `is` instead of `==` prevents some custom classes
from resolving to `True` when compared with `None`.

7. Comparing with `None`
------------------------

Usually the following comparison will be giving error, because we compared a variable which is `None` with an integer - 

```python
a = None
a > 10
```

To avoid this, use `and` or `or` operators because the execution order between the clauses is followed from left to right,
and that can be used to avoid these inintentional errors.

In case of `or` -

```python
a = None
b = a is None or a > 10
``` 

In case of `and` -

```python
a = None
b = a is not None and a > 10
```

8. Highest female name count
----------------------------

Example of how to use `and` with `None`.

```python
# name_counts is a dictionary with name counts for each of the female legislator
max_value = None
for k in name_counts:
    count = name_counts[k]
    if max_value is None or max_value < count:
         max_value = count
```

9. The `items()` method
-----------------------

Using `items()` method of `dictionary` class, we can access key-value pair in a tuple format.

```python
for key, value in mydict.items():
    ...
```

10. Finding the most common female names
----------------------------------------

From an earlier screen, we know that the most common female names occur `2` times in `name_counts`.
We can extract any keys in `name_counts` that have the associated value `2`.

```python
top_female_names = []
for name, count in name_counts.items():
    if count == 2:
        top_female_names.append(name)

# List comprehension
top_female_names = [k for k, v in name_counts.items() if v == 2]
```

11. Finding the most common male names
--------------------------------------

Everything so far in one excercie.

- Make a dictionary of male names, where keys are names and values are occurrances
- Find what is the highest count on occurrances
- Append any names which occur that many times

```python
top_male_names = []
male_name_counts = {}

name_col = 1

# Make a dictionary of male names
for legislator in legislators:
    name = legislator[name_col]
    if name in male_name_counts:
        male_name_counts[name] += 1
    else:
        male_name_counts[name] = 1

# Find what is the highest count
highest_male_count = None
for key in male_name_counts:
    if highest_male_count is None or highest_male_count < male_name_counts[key]:
        highest_male_count = male_name_counts[key]

# Append any keys whose values are equal to the highest count
for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
```
