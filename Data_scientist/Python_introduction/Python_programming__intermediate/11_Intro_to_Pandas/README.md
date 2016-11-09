Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Introduction to Pandas
===================================================================================================================

1. Introduction to Pandas
-------------------------

Pandas is a library that unifies the most common workflows that data analysts and data scientists previously relied 
on many different libraries for.

To represent tabular data, Pandas uses a custom data structure called a **DataFrame**. A DataFrame is a highly 
efficient, 2-dimensional data structure that provides a suite of methods and attributes to quickly explore, analyze,
and visualize data.

One of the biggest advantages that Pandas has over NumPy is the ability to store mixed data types in rows and columns.
Pandas DataFrames can also handle missing values gracefully using a custom object, `NaN`, to represent those values.

2. The dataset
--------------

A dataset from United States Department of Agriculture (USDA), contains nutritional information on the most common
foods Americans consume. Out of many columns, **some** of them are -

NDB_No | unique id of the food.
:---: | :---: |
Shrt_Desc | name of the food.
Water_(g) | water content in grams.
Energ_Kcal | energy measured in kilo-calories.
Protein_(g) | protein measured in grams.
Cholestrl_(mg) | cholesterol in milligrams.

3. Read in a CSV file
---------------------

Use `read_csv()` where you can pass the string of the name of the file. 

```python
crime_rates = pandas.read_csv("crime_rates.csv")
```

The object returned is a `<class 'pandas.core.frame.DataFrame'>` type object.

4. Exploring the `DataFrame`
---------------------------

`head(n)` method will return first n rows of the DataFrame. `head()` (with no argument) returns first 5 rows.

```python
food_info = pandas.read_csv("food_info.csv")
print(food_info.head(3))
```

Will give you the output - 

```
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85   
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85   
2    1003      BUTTER OIL ANHYDROUS       0.24         876         0.28   

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06   
1          81.11     2.11            0.06           0.0           0.06   
2          99.48     0.00            0.00           0.0           0.00   

        ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
0       ...          2499.0      684.0        2.32        1.5      60.0   
1       ...          2499.0      684.0        2.32        1.5      60.0   
2       ...          3069.0      840.0        2.80        1.8      73.0   

   Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)  
0          7.0      51.368       21.021        3.043           215.0  
1          7.0      50.489       23.426        3.012           219.0  
2          8.6      61.924       28.732        3.694           256.0  

[3 rows x 36 columns]
```

`shape` attribute can give you the dimensions of the `DataFrame`. 

```python
print(food_info.shape)          # (8618, 36)
print(food_info.shape[0])       # 8618
print(food_info.shape[1])       # 36
```

5. Indexing
-----------

Pandas uses the values in the first row (also known as the header) for the column labels and the row number 
for the row labels. row indices start from 0, column indices are strings.

6. Series
---------

The **Series** object is a core data structure that Pandas uses to represent rows and columns. A Series is 
a labelled collection of values similar to the NumPy vector. When you select a row from a DataFrame, instead 
of just returning the values in that row as a list, Pandas returns a Series object that contains the column 
labels as well as the corresponding values.

7. Selecting a row
------------------

`loc[]` method (?) allows you to select rows by rows label. 

```python
print(food_info.loc[99])
```

Will give the output -

```python
NDB_No                                  1111
Shrt_Desc          MILK SHAKES THICK VANILLA
Water_(g)                              74.45
.
.
.
FA_Poly_(g)                            0.113
Cholestrl_(mg)                            12
Name: 99, dtype: object
``` 

And, index error in case of -

```python
print(food_info.loc[8620])                  # KeyError: 'the label [8620] is not in the [index]'
```

8. Datatypes
------------

To access the types for each column, use the DataFrame attribute dtypes to return a Series containing each 
column name and its corresponding type.

```python
print(food_info.dtypes)
```

Will give you -

```python
NDB_No               int64
Shrt_Desc           object
Water_(g)          float64
.
.
.
FA_Poly_(g)        float64
Cholestrl_(mg)     float64
dtype: object
```

And, these `dtype`s are accessible with `[]` notation, like -

```python
print(food_info.dtypes[0])          # int64
```

9. Selecting multiple rows
--------------------------

`loc[m:n]` notation can be used to select multiple rows. Note that unlike slicing lists in Python, a slice of 
a DataFrame using `loc[]` **will include both the start and the end row** (i.e. `m`th and `n`th row).

```python
food_info.loc[3:6]                  # row no. 3, 4, 5 and 6
```

`loc[]` can also accept a list of indices as -

```python
two_five_ten = [2,5,10] 
food_info.loc[two_five_ten]         # row no. 2, 5 and 10
```

10. Selecting individual columns
--------------------------------

When accessing a column in a DataFrame, Pandas returns a `Series` object containing the row label and each row's value 
for that column. To access a single column, use bracket notation and pass in the column name as a string -

```python
# You can instead access a column by passing in a string variable.
col_name = "NDB_No"
ndb_col = food_info[col_name]
```

11. Selecting multiple columns by name
--------------------------------------

Similar to selecting multiple rows (of course `:` notation is not applicable, only list notation can be used). Returns
`DataFrame` object, and **not** a `Series`.

```python
columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
```

12. Practice
------------

Select and display only the columns that use grams for measurement (those that end with `"(g)"`). 

```python
print(food_info.columns)
print(food_info.head(2))
col_names = food_info.columns.tolist()
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))
```

