Data Scientist / Python Introduction / Python Programming: Beginner / Files and Loops
=====================================================================================

1. Overview
-----------

2. Opening files
----------------
- `open()` function

`open()` function returns a file object. Syntax -

```python
file_obj = open("story.txt", "r")
```

file_obj doesn't contain the actual contents of the file. It is an interface.

3. Reading in files
-------------------
- `read()` function

```python
txt = file_obj.read()
print(txt) # prints contents
```

4. Splitting
------------
- `split()` function

5. Loops
--------

6. Practice: Loops
------------------

7. List of lists
----------------

```python
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)           # [['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828']]
print(final_list[0])        # ['Albuquerque', '749']
print(final_list[1])        # ['Anaheim', '371']
print(final_list[2])        # ['Anchorage', '828']
```

8. Practice: Splitting elements in a list
-----------------------------------------

9. Accessing elements in a list of lists
----------------------------------------

10. Looping through a list of lists
-----------------------------------

11. Challenge
-------------
