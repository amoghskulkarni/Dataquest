Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Getting started with NumPy
=======================================================================================================================

1. The dataset
--------------

`world_alcohol.csv`, which contains data on how much alcohol is consumed per capita in each country.

Year | WHO Region | Country | Beverage Types | Display value
:---:|:---:|:---:|:---:|:---:|
`1986` | `'Western Pacific'` | `'Viet Nam'` | `'Wine'` | `0`
`1986` | `'Americas'` | `'Uruguay'` | `'Other'` | `0.5`

2. Lists of lists
-----------------

While extracting single values and rows is easy with lists of lists, it's cumbersome to compute statistics 
and extract columns. If we wanted to compute the average of the `Years` column, here's what we'd have to do -

```python
import csv
f = open("world_alcohol.csv")
reader = csv.reader(f)
world_alcohol = list(reader)

years = []
for row in world_alcohol:
    years.append(row[0])

years = years[1:]

total = 0
for year in years:
    total = total + float(year)

avg_year = total / len(years)
```

3. Introducing NumPy
--------------------

NumPy can be used to create and manipulate multidimensional data. In this case, we'll be creating _matrix_ of
our data.

4. Using NumPy
--------------

Using `genfromtxt()` method of NumPy, csv files can be directly read into matrices.

```python
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
```

5. Creating arrays
------------------

Using `array()` method of NumPy, n-D arrays can be created.

```python
vector = numpy.array([5, 10, 15, 20])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
```

6. Array shape
--------------

NumPy arrays have `shape` property which returns their shape in the form of tuples.

```python
vector = numpy.array([1, 2, 3, 4])
print(vector.shape)                 # (4,)

matrix = numpy.array([[5, 10, 15], [20, 25, 30]])
print(matrix.shape)                 # (2,3)
```

7. Data types
-------------

Each value in a NumPy _array_ has to have the **_same_** data type. This is why they have
`dtype` property which gives the datatype of their elements. It is `numpy.dtype` object.

```python
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)          # float64
```

8. Inspecting the data
----------------------

Here's how the first few rows of `world_alcohol` look:

```python
array([[             nan,              nan,              nan,              nan,              nan],
       [  1.98600000e+03,              nan,              nan,              nan,   0.00000000e+00],
       [  1.98600000e+03,              nan,              nan,              nan,   5.00000000e-01]])
```

NumPy's `genfromtxt()` cannot read the datafileds which are strings, so it uses `nan` to represent
them. When the values are not available, it uses `na`. 

9. Reading in data properly
---------------------------

Our data wasn't read in properly, which resulted in NumPy trying to convert strings to floats, and nan values.
We can fix this by specifying in the `genfromtxt()` method that we want to read in all the data as **strings**.
While we're at it, we can also specify that we want to skip the header row of `world_alcohol.csv`.

```python
# U75 specifies the data is in unicode string
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
```

10. Indexing arrays
-------------------

Syntax `arr[m][n]` as well as `arr[m,n]` works well with NumPy arrays, where you want to access (m,n)th element
of the array. 

11. Slicing arrays
------------------

We can slice vectors very similarly to how we slice Python lists - 

```python
vector = numpy.array([5, 10, 15, 20])
print(vector[0:3])
```

In addition to this, NumPy also provides us the tools to slice matrics (higher dimension arrays).  
Matrix slicing is a bit more complex, and has four forms -

- When we want to select one entire dimension, and a single element from the other.

```python
matrix = numpy.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[:,1])          # [10, 25, 40]
```

- When we want to select one entire dimension, and a slice of the other.

```python
print(matrix[:,0:2])
# [
#     [5, 10],
#     [20, 25],
#     [35, 40] 
# ]
```

- When you want to select a slice of one dimension, and a single element from the other.

```python
print(matrix[1:3,1])
# [
#     [25], 
#     [40]
# ]
```

- When we want to slice both dimensions.

```python
print(matrix[1:3,0:2])
# [
#     [20, 25],
#     [35, 40]
# ]
```


