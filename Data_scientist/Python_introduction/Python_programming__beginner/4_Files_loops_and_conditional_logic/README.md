Data Scientist / Python Introduction / Python Programming: Beginner / Challenge: Files, Loops, and Conditional Logic
====================================================================================================================

1. How challenges work
----------------------

2. Unisex names
---------------

- Dataset used: [FiveThirtyEight article](http://fivethirtyeight.com/features/there-are-922-unisex-names-in-america-is-yours-one-of-them/)
- csv file give is: `dq_unisex_names.csv`

Contents

```python
Casey,176544.328149
Riley,154860.66517300002
Jessie,136381.830656
Jackie,132928.78874000002
Avery,121797.41951600001
Jaime,109870.18729000002
Peyton,94896.39521599999
```

3. Read the file into a string
------------------------------

```python
f = open("dq_unisex_names.csv", "r")
data = f.read()
```

4. Convert the string into a list
---------------------------------

- Each row contains a datapoint, which becomes an element in the list

```python
f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split("\n")
```

`data_list` looks something like -

```python
['Casey,176544.328149', 'Riley,154860.66517300002', 'Jessie,136381.830656', ...]
```

5. Convert the list of strings to a list of lists
-------------------------------------------------

- Convert using `split()` over `,`

```python
string_data = []
for data_list_entry in data_list: 
    string_data.append(data_list_entry.split(","))
```

`string_data` looks something like -

```python
[['Casey', '176544.328149'], ['Riley', '154860.66517300002'], ['Jessie', '136381.830656'], ...]
```

6. Convert numerical values
---------------------------

```python
numerical_data = []
for d in string_data:
    numerical_data.append([d[0], float(d[1])])
```

7. Filter the list
------------------

```python
thousand_or_greater = []
for d in numerical_data:
    if d[1] >= 1000:
        thousand_or_greater.append(d[0])
```
