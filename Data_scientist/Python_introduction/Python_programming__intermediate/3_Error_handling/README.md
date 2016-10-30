Data Scientist / Python Introduction / Python Programming: Intermediate / Error handling
========================================================================================

1. The dataset
--------------

last\_name | first\_name | birthday | gender | type | state | party
:---:|:---:|:---:|:---:|:---:|:---:|:---:|
'Bassett' | 'Richard' | '1745-04-02' | 'M' | 'sen' | 'DE' | 'Anti-Administration'
'Bland' | 'Theodorick' | '1742-03-21' | | 'rep' | 'VA' | 
'Burke' | 'Aedanus' | '1743-06-16' | | 'rep' | 'SC' |
'Carroll' | 'Daniel' | '1730-07-22' | 'M' | 'rep' | 'MD' |

2. Sets
-------

Sets are collection of unique objects, and it doesn't have any index associated with elements in it. 

```python
unique_animals = set(["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"])
print(unique_animals)           # {'Hippo', 'Cat', 'Dog'}
```

`add()` and `remove()` for adding and removing the elements to and from the set. 

The formed set can again be converted into a list by using `list()` method.

3. Exploring the dataset
------------------------

For discovering valuable things such as missing values, values that don't make any intuitive sense
or recurring themes from the data can be found out using `set` of values.

4. Missing values
-----------------

Some datasets can have misssing values which can be dealt with - 

- Removing the data point
- Initializing the data point with a default value
- Initializing the data point with a calculated value

5. Parsing birth years
----------------------

Change format of the value of birthday from `"YYYY-MM-DD"` to `["YYYY", "MM", "DD"]`. Use `split()`.

6. Try/Except blocks
--------------------

Basics of try-except blocks.

7. Exception instances
----------------------

When the Python interpreter creates an exception, it actually creates an instance of the `Exception` class (!).

```python
try:
    int('')
except Exception as exc:
    print(type(exc))            # Prints type of Exception
```

