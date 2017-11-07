# Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Pandas Internals: Series

## 1. Data structures

-----

The three key data structures in pandas are:

- `Series` objects (collections of values)
- `DataFrames` (collections of Series objects)
- `Panels` (collections of DataFrame objects)

`Series` objects use NumPy arrays for fast computation, but add valuable features to them for analyzing data. While NumPy arrays use an integer index, for example, Series objects can use other index types, such as a string index. Series objects also allow for mixed data types, and use the `NaN` Python value for handling missing values.

Some of the columns of Fandango dataset - 

- `FILM` - Film name
- `RottenTomatoes` - Average critic score on Rotten Tomatoes
- `RottenTomatoes_User` - Average user score on Rotten Tomatoes
- `RT_norm` - Average critic score on Rotten Tomatoes (normalized to a 0 to 5-point system)
- `RT_user-norm` - Average user score on Rotten Tomatoes (normalized to a 0 to 5-point system)
- `Metacritic` - Average critic score on Metacritic
- `Metacritic_User` - Average user score on Metacritic

### Instructions

Read and print the first 2 rows -

```python
fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2)
```

Output is - 

```python
                             FILM  RottenTomatoes  RottenTomatoes_User  \
0  Avengers: Age of Ultron (2015)              74                   86   
1               Cinderella (2015)              85                   80   

   Metacritic  Metacritic_User  IMDB  Fandango_Stars  Fandango_Ratingvalue  \
0          66              7.1   7.8             5.0                   4.5   
1          67              7.5   7.1             5.0                   4.5   

   RT_norm  RT_user_norm         ...           IMDB_norm  RT_norm_round  \
0     3.70           4.3         ...                3.90            3.5   
1     4.25           4.0         ...                3.55            4.5   

   RT_user_norm_round  Metacritic_norm_round  Metacritic_user_norm_round  \
0                 4.5                    3.5                         3.5   
1                 4.0                    3.5                         4.0   

   IMDB_norm_round  Metacritic_user_vote_count  IMDB_user_vote_count  \
0              4.0                        1330                271107   
1              3.5                         249                 65709   

   Fandango_votes  Fandango_Difference  
0           14846                  0.5  
1           12640                  0.5  
```

## 2. Integer Indexes

-----

By default, pandas indexes each individual Series object in a DataFrame with the integer data type. Each value 
in the Series has a unique integer index, or position. Like most Python data structures, the Series object uses 
_0-indexing_. The indexing ranges from `0` to `n-1`, where `n` is the number of rows.

### Instrcutions 

- Select the `FILM` column, assign it to the variable `series_film`, and print the first five values.
- Then, select the `RottenTomatoes` column, assign it to the variable `series_rt`, and print the first five values.

```python
series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]

# Works
# print(series_film[0:5])
# print(series_rt[0:5])

# Also works
print(series_film.loc[0:5])
print(series_rt.loc[0:5])
```

## 3. Custom Indexes

-----

If we only have 2 `Series` objects, 1 for names and another for scores, and they happen to be large lists; the finding
operations become cumbersome. So we create a new `Series` object which has the movie names as indices and values are the 
scores.

```python
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = Series(index=film_names, data=rt_scores)
``` 

## 4. Integer Index Preservation

-----

Even though we specified that the `Series` object uses a custom string index, the object still has an internal integer 
index that we can use for selection. When it comes to indexes, Series objects act like both dictionaries and lists.

### Instructions

Assign the values in `series_custom` at indexes `5` through `10` to the variable `fiveten`. Then, print `fiveten` to 
verify that you can still use integer values for selection.

```python
series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:11]
print(fiveten)
```

## 5. Reindexing

-----

Reindexing is the pandas way of modifying the alignment between labels (indexes) and the data (values). 
The [`reindex()`](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.reindex.html) method allows us 
to specify a different order for the labels (indexes) in a `Series` object. 
This method takes in a list of strings corresponding to the order we'd like for that Series object.

We can use the `reindex()` method to sort series_custom alphabetically by film.

```python
original_index = series_custom.index

sorted_index = sorted(original_index)

sorted_by_index = series_custom.reindex(sorted_index)
```

## 6. Sorting

-----

To make sorting easier, pandas comes with a [`sort_index()`](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_index.html) 
method that sorts a Series by index, and a [`sort_values()`](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_values.html) 
method that sorts a Series by its values.

In both cases, pandas preserves the link between each element's index (film name) and value (score). We call this data alignment, 
which is a key tenet of pandas that's incredibly important when analyzing data. Pandas allows us to assume the linking will be preserved, 
unless we specifically change a value or an index.

```python
print(series_custom[0:10])
print("____")

sc2 = series_custom.sort_index()
print(sc2[0:10])
print("____")

sc3 = series_custom.sort_values()
print(sc3[0:10])
```

Gives output -

```python
Avengers: Age of Ultron (2015)    74
Cinderella (2015)                 85
Ant-Man (2015)                    80
Do You Believe? (2015)            18
Hot Tub Time Machine 2 (2015)     14
The Water Diviner (2015)          63
Irrational Man (2015)             42
Top Five (2014)                   86
Shaun the Sheep Movie (2015)      99
Love & Mercy (2015)               89
dtype: int64
____
'71 (2015)                    97
5 Flights Up (2015)           52
A Little Chaos (2015)         40
A Most Violent Year (2014)    90
About Elly (2015)             97
Aloha (2015)                  19
American Sniper (2015)        72
American Ultra (2015)         46
Amy (2015)                    97
Annie (2014)                  27
dtype: int64
____
Paul Blart: Mall Cop 2 (2015)     5
Hitman: Agent 47 (2015)           7
Hot Pursuit (2015)                8
Fantastic Four (2015)             9
Taken 3 (2015)                    9
The Boy Next Door (2015)         10
The Loft (2015)                  11
Unfinished Business (2015)       11
Mortdecai (2015)                 12
Seventh Son (2015)               12
dtype: int64
```

## 7. Transforming Columns With Vectorized Operations

-----

Arithmatic element-wise operations

- `+`, `-`, `*` or `/` can be used to transform each of the values in a series object.
  - Usually scalars are used with these operations
- Numpy operations such as `np.add(series1, series2)
  - Two serieses are element-wise added

The original DataFrame contains the column `RT_norm`, which represents a normalized score (from 0 to 5) of 
the Rotten Tomatoes average critic score. Let's use vectorized operations to normalize `series_custom` back to the 0-5 scale. 

### Instructions

- Normalize `series_custom` (which is currently on a 0 to 100-point scale) to a 0 to 5-point scale by dividing each value by 20.
- Assign the new normalized Series object to `series_normalized`.

```python
print(series_custom[0:5])
print("_____")

series_normalized = series_custom / 20

print(series_normalized[0:5])
```

Gives output -

```python
Avengers: Age of Ultron (2015)    74
Cinderella (2015)                 85
Ant-Man (2015)                    80
Do You Believe? (2015)            18
Hot Tub Time Machine 2 (2015)     14
dtype: int64
_____
Avengers: Age of Ultron (2015)    3.70
Cinderella (2015)                 4.25
Ant-Man (2015)                    4.00
Do You Believe? (2015)            0.90
Hot Tub Time Machine 2 (2015)     0.70
dtype: float64
```

## 8. Comparing and Filtering

-----

Similar to a `DataFrame`, a list of boolian values (which is of the same length of that of the Series) will filter the series.
We can specify filtering criteria in different variables, then chain them together with the `and` operator (`&`) or the `or` operator (`|`).

```python
criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]
any_one_criteria = series_custom[criteria_one | criteria_two]
```

## 9. Alignment

-----

One of pandas' core tenets is **data alignment**. Series objects align along indices, and DataFrame objects align along both indices 
and columns. With Series objects, pandas implicitly preserves the link between the index labels and the values across operations and 
transformations, unless we explicitly break it. With DataFrame objects, the values link to the index labels and the column labels. 
Pandas also preserves these links, unless we explicitly break them (by reassigning or editing a column or index label, for example).

### Instructions

- `rt_critics` and `rt_users` are Series objects containing the average ratings from critics and users for each film.
- Both Series objects use the same custom string index, which they base on the film names. Use the Python arithmetic operators to 
  return a new Series object, `rt_mean`, that contains the mean ratings from both critics and users for each film.

```python
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_critics + rt_users) / 2 
```

