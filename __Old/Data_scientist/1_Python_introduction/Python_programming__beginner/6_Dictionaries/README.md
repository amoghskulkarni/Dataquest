Data Scientist / Python Introduction / Python Programming: Beginner / Dictionaries
==================================================================================

1. The dataset
--------------

- List of 365 elements

```python
["Sunny", "Sunny", "Sunny", ..., "Fog"]
```

2. Dictionaries
---------------

- Introduction to Dictionaries in Python

- Syntax

- Adding the key-value pair and accessing the values

- Key and values can any type of objects i.e. strings, integer or float

3. Practice: Populating a dictionary
------------------------------------

```python
students = {}
students["Jerry"] = 60
```

4. Practice: Indexing a dictionary
----------------------------------

```python
students["Tom"]
```

5. Defining a dictionary with values
------------------------------------

```python
students = {
    "Tom": 60,
    "Jim": 70,
    "Sue": 85,
    "Ann": 80
}
```

6. Modifying dictionary values
------------------------------

```python
students["Tom"] = students["Tom"] + 5
```

7. The `in` statement and dictionaries
--------------------------------------

We can use the `in` statement to check if a `key` occurs in a dictionary

```python
planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
print jupiter_found         # True
```

8. The `else` statement
-----------------------

Huh? (didn't see this one coming in "dictionaries" lesson)

9. Practice: The `else` statement
---------------------------------

10. Counting with dictionaries
------------------------------

11. Counting the weather
------------------------

Count up how many times each type of weather occurs in the `weather` list, and store the results in `weather_counts`.

```python
weather_counts = {}

for w in weather:
    if w in weather_counts:
        weather_counts[w] += 1
    else:
        weather_counts[w] = 1
```
