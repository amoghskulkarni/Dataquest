Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Computation with NumPy
===================================================================================================================

1. The dataset
--------------

`world_alcohol.csv`, which contains data on how much alcohol is consumed per capita in each country.

Year | WHO Region | Country | Beverage Types | Display value
:---:|:---:|:---:|:---:|:---:|
`1986` | `'Western Pacific'` | `'Viet Nam'` | `'Wine'` | `0`
`1986` | `'Americas'` | `'Uruguay'` | `'Other'` | `0.5`

2. Array comparisons
--------------------

NumPy arrays can be compared to an object - the object will be compared with each and every element of the array 
and an array of same dimensions containing `True` and `False` will be returned (according to the result of each
comparison).

```python
vector = numpy.array([5, 10, 15, 20])
vector == 10                            # [False, True, False, False]
```

3. Selecting elements
---------------------

Elements in NumPy array can be selected using an array of same dimension containing boolean values (`True` and 
`False`). The elements corresponding to `True` will be selected.

```python
vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)           # [False, True, False, False]

print(vector[equal_to_ten])             # [10]
```

This is especially handy when we have to select rows depending upon the values of a certain column.

```python
matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
    second_column_25 = (matrix[:,1] == 25)          # [False, True, False]
    print(matrix[second_column_25, :])              # [20, 25, 30]
    print(matrix[second_column_25, 2])              # [30]
```

4. Comparisons with multiple conditions
---------------------------------------

NumPy arrays can be operated as if they are scalars - when operated upon with scalar operator, element-by-element
operation is performed.

```python
a = numpy.array([True, False, False, False])
b = numpy.array([False, True, False, False])
a & b                   # [False, False, False, False]
a | b                   # [True, True, False, False]
```

It also holds true with the arithmatic operations - addition, subtraction, multiplication, division, etc. 

Using this we can compare an array using multiple conditions. It is critical to put each one in parentheses 
in this case. 

```python
vector = numpy.array([5, 10, 15, 20])
equal_to_ten_and_five = (vector == 10) & (vector == 5)          # [False, False, False, False]
equal_to_ten_or_five = (vector == 10) | (vector == 5)           # [True, True, False, False]
```

5. Replacing values
-------------------

The above way of selecting elements using array of booleans is just a way of accessing specific indices according
to boolean values. You can either read or write after you get the access to them.

```python
vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)

print(vector[equal_to_ten_or_five])                             # [5, 10]

vector[equal_to_ten_or_five] = 50                               # [50, 50, 15, 20]
```

The following code snippet will replace all instances of the string `1986` in the first column, and all instances of
the string `Wine` from the third column with `2014` and `Grog` respectively.

```python
first_col_1986 = (world_alcohol[:, 0] == '1986')
world_alcohol[first_col_1986, 0] = '2014'

third_col_Wine = (world_alcohol[:, 3] == 'Wine')
world_alcohol[third_col_Wine, 3] = 'Grog'
```

6. Replacing empty strings
--------------------------

For now, every element in the dataset `world_alcohol` is a string, but the column 5 is of `Display value` which is
a numerical data. We want to convert it to the `Float` but before that have to make sure that it only includes integers.
Some rows have `''` as their 5th element, which we need to replace with `0`.

```python
is_value_empty = (world_alcohol[:, 4] == '')
world_alcohol[is_value_empty, 4] = '0'
```

7. Converting data types
------------------------

We can convert the data type of an array using the `astype()` method. Here's an example -

```python
vector = numpy.array(["1", "2", "3"])
vector = vector.astype(float)               # [1.0, 2.0, 3.0]
```

In the `world_alcohol` dataset, convert 5th column to float. Notice that we are accessing the same dataset,
even if we save the 5th column inside another variable (pass by reference).

```python
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)
```

8. Computing with NumPy
-----------------------

- sum()
- mean()
- max()

```python
vector = numpy.array([5, 10, 15, 20])
vector.sum()                                # 50
```

The following code snippet will extract the alcohol consumption from the `world_alcohol` dataset (5th column)
and then run the `sum()` and `mean()` methods on it.

```python
alcohol_consumption = world_alcohol[:,4]    # Extraction of the column

total_alcohol = alcohol_consumption.sum()   # Running the methods 
average_alcohol = alcohol_consumption.mean()
```

With a matrix, we have to specify an additional keyword argument `axis`. The axis dictates which dimension 
we perform the operation on. `1` means that we want to perform the operation on each row, and `0` means 
on each column. (TODO: How does `axis` work in case of more than 2 dimensions?)

```python
matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
matrix.sum(axis=1)                          # [30, 75, 120]
```

9. Total alcohol consumption in a year
--------------------------------------

Given a country and a year, we can find all the relevant entries from the dataset and add up their 5th column,
(which is related to alcohol consumption) to find out total alcohol consumption in the country in that year.

```python
# Find the rows where first column is "1986" and third column is "Canada"
canada_1986 = world_alcohol[(world_alcohol[:, 0] == "1986") & (world_alcohol[:, 2] == "Canada"), :]

# After finding those rows, replace the fifth column of the rows where the value is '' with "0" 
canada_1986[(canada_1986[:, 4] == ''), 4] = "0"

# Convert their fifth column to float datatype
canada_alcohol = canada_1986[:, 4].astype(float)

# Sum them up
total_canadian_drinking = canada_alcohol.sum()
```

10. Calculating consumption for each country
--------------------------------------------

Same thing for each country.

```python
totals = {}
for country in countries:
    country_1986 = world_alcohol[(world_alcohol[:, 0] == "1989") & (world_alcohol[:, 2] == country), :]
    country_1986[(country_1986[:, 4] == ''), 4] = "0"
    country_alcohol = country_1986[:, 4].astype(float)
    total_country_drinking = country_alcohol.sum()
    totals[country] = total_country_drinking
```

11. Finding the country that drinks the most
--------------------------------------------

Iterate over the dictionary that is populated above, and find out the key with the greatest value. Trivial.

12. NumPy strengths and weaknesses
----------------------------------

Strengths -

- It's easy to perform computations on data.
- Data indexing and slicing is faster and easier.
- Data types can be converted quickly.

Limitations -

- A whole array has to be the same datatype, which makes it cumbersome to work with many datasets.
- Columns and rows have to be referred to by number, which gets confusing when you go back and forth from 
column name to column number.

