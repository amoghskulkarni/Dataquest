# Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Pandas Internals: DataFrame

## Introduction

`Series` objects maintain data alignment between values and their index labels. Because `DataFrame` objects are basically 
collections of `Series` objects, they maintain alignment along both columns and rows.

Pandas dataframe share a row index across columns. By default, this is an _integer_ index. Pandas enforces this shared row 
index by throwing an error if we read in a CSV file with columns that contain a different number of elements.

Index values appear in the leftmost column of a `DataFrame` and we can use `index` attribute to access the index values 
directly.

## Using Integer Indexes to Select Rows

With `Series`, each unique index value refers to a data value. With dataframes, however, each index value refers to an entire row. 

```python
# First five rows
fandango[0:5]
# From row at 140 and higher
fandango[140:]
# Just row at index 50
fandango.iloc[50]
# Just row at index 45 and 90
fandango.iloc[[45,90]]
```

## Using Custom Indexes

The dataframe object has a `set_index()` method that allows us to pass in the name of the column we want pandas to use as the 
Dataframe index. By default, pandas will create a new dataframe, index it by the values in the column we specify, then drop that column.

- `inplace`: If set to `True`, this parameter will set the index for the current, "live" dataframe, instead of returning a new dataframe.
- `drop`: If set to `False`, this parameter will keep the column we specified as the index, instead of dropping it.

## Using a Custom Index For Selection

We can select a row by film name instead of row number (which is the default integer index). We can select rows using the custom index by either:

- Using the `loc[]` method (the same way we would the `iloc[]` method)
- Creating a slice using bracket notation

```python
# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]
```

## Apply() Logic Over the Columns in a Dataframe

Recall that a dataframe object represents both rows and columns as `Series` objects. The `apply()` method in pandas allows us to specify Python 
logic that we want to evaluate over the Series objects in a dataframe. E.g. - 

- Calculate the standard deviations for each numeric column
- Lowercase all film names in the `FILM` column

The `apply()` method requires us to pass in the vectorized operation we want to apply over each Series object. The method runs over the 
dataframe's columns by default. If the vectorized operation usually returns a single value (such as the NumPy `std()` function), it will 
return a Series object containing the computed value for each column. If it usually returns a value for each element 
(such as multiplying or dividing by 2), it will transform all of the values and return them as a dataframe.

For these operations to work, the column datatypes should match (or it should be specifically given which columns are to be operated upon).
For separating the columns having values of same datatypes - 

```python
# returns the data types as a Series
types = fandango_films.dtypes

# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index

# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]
```

Now, use `apply()` on `float_df` as instructed.

## Apply() Logic Over Columns: Practice

Recall that the NumPy `std()` method returns a single computed value when we apply it over a Series. If we use a NumPy function that returns 
a value for each element in a Series, we can transform all of the values in each column and return a dataframe with those new values instead.

```python
float_df.apply(lambda x: x*2)
```

## Apply() Over Dataframe Rows

So far we've used the default behavior of the `apply()` method, which operates over the columns in a Dataframe. To apply a function over the 
rows in a dataframe (which pandas treats as Series objects), we need to set the `axis` parameter to `1`.

```python
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]

# returns a Series object containing the standard deviation of each movie's ratings from RT_user_norm and Metacritic_user_nom.
rt_mt_user.apply(lambda x: np.std(x), axis=1)
```

P.S. Standard deviations are measure of spread of the data. So the above code shows how much the scores vary.




