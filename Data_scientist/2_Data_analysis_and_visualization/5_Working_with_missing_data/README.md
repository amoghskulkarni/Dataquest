Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Working with missing data
======================================================================================================================

1. Introduction
---------------

In this mission, we'll clean and analyze data on passenger survival from the Titanic. Each row contains information 
for a specific Titanic passenger. Here are some of the columns -

- `pclass` -- The passenger's cabin class from 1 to 3 where 1 was the highest class
- `survived` -- 1 if the passenger survived, and 0 if they did not.
- `sex` -- The passenger's gender
- `age` -- The passenger's age
- `fare` -- The amount the passenger paid for their ticket
- `embarked` -- Either C, Q, or S, to indicate which port the passenger boarded the ship from.

2. Finding the missing data
---------------------------

`None` is a Python keyword, whereas `NaN` is used by pandas to refer a quantity which is "not-a-number". Together,
these two can be called _null_ values.

`isnull()` method of `Series` returns a `Series` object which is a list of boolean values.

```python
sex = titanic_survival["sex"]
sex_is_null = pandas.isnull(sex)                # Will return a Series object of boolean values
```

This `Series` object containing boolean values can be used to choose those values which are not _null_.

```python
sex_null_true = sex[sex_is_null]
```

To find out `age` values of the Titanic passengers -

```python
age = titanic_survival["age"]
age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)             # Will give you the number of entries that have a valid number in age column
```

3. What's the big deal with the missing data
--------------------------------------------

The result of the following operation to calculate average age of the survivors of Titanic will be `NaN`, as some
of the values are `NaN`.

```python
mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])
```

Sanitizing data is crucial to avoid such scenarios. 

To take only those entries which have `age` as a valid number, we need the inverse of the `Series` object that gets
returned from `isnull()`. I.e. -

```python
age_is_null = pd.isnull(titanic_survival["age"])
valid_ages = titanic_survival["age"][age_is_null == False]
```

Take average of `valid_ages`.

4. Easier ways to do math
-------------------------

Many pandas methods automatically filter for missing data. We can use `Series.mean()` method for the task which we did
in the above code.

```python
correct_mean_age = titanic_survival["age"].mean()
```

5. Calculating summary statistics
---------------------------------

`pclass` column has one of the 3 values - `1` for first class, `2` for second class and `3` for third class.

We can calculate average fare for all the three classes by filtering the rows of a particular `pclass` value and then
using `mean()` method on them.

```python
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["pclass"] == this_class]
    pclass_fares = pclass_rows["fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
```

6. Making pivot tables
----------------------

Pivot tables provide an easy way to subset by one column and then apply a calculation like a sum or a mean. 

Pivot tables first group and then apply a calculation. In the previous screen, we actually made a pivot table manually 
by grouping by the column `pclass` and then calculating the mean of the `fare` column for each class.

`DataFrame.pivot_table()` method can be used to do exact same thing as -

```python
fares_by_class = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)
```

- The first parameter of the method, `index` tells the method which column to group by. 
- The second parameter `values` is the column that we want to apply the calculation to.
- `aggfunc` specifies the calculation we want to perform.  
The default for the aggfunc parameter is actually the mean, so if we're calculating this we can omit this parameter.

The method returns a `Series` object.

7. More complex pivot tables
----------------------------

A list of the columns which you want to perform the `aggfunc` operation on can be given to `values` option.

A pivot table that calculates the total fares collected (`fare`) and total number of survivors (`survived`) for each 
embarkation port (`embarked`).

```python
port_stats = titanic_survival.pivot_table(index="embarked", values=["fare","survived"], aggfunc=np.sum)
```

Output is -

```python
                fare  survived
embarked                      
C         16830.7922     150.0
Q          1526.3085      44.0
S         25033.3862     304.0
```

8. Drop missing values
----------------------

`DataFrame.dropna()` method can be used to drop rows / columns that contain _null_ values.

You can specify `axis` parameter to the method to drop either row or column. `0` value to `axis` drops rows and `1`
drops columns. Default is `0`. Alternatively, you can give `index` and `columns` values to `axis` parameter to gets
the similar result as `0` and `1` respectively.

```python
drop_na_rows = titanic_survival.dropna(axis=0)
```

`subset` parameter can be used to provide the names of the columns which are to be taken into consideration.

Following code only drops those lines which contain _null_ values in `age` and `sex` columns.

```python
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["age", "sex"])
``` 

9. Using `iloc` to access rows by position
------------------------------------------

The rows in in `DataFrame` are referenced by using `DataFrame.loc[]`, which uses labels of the rows to refer to the
rows.

If you have performed some operations on your `DataFrame` (like filtering using `isnull()` or sorting using `sort()`),
you get a new `DataFrame` which has rows with the labels which are not in order. E.g. these are the first 5 rows of the
`DataFrame` where the labels of the rows are not in order -

||pclass|survived|name|sex|age
|:---:|:---:|:---:|:---:|:---:|:---:
14|1.0|1.0|Barkworth, Mr. Algernon Henry Wilson|male|80.0
61|1.0|1.0|Cavendish, Mrs. Tyrell William (Julia Florence...|female|76.0
1235|3.0|0.0|Svensson, Mr. Johan|male|74.0
135|1.0|0.0|Goldschmidt, Mr. George B|male|71.0
9|1.0|0.0|Artagaveytia, Mr. Ramon| |   

In this `DataFrame`, you can reference the first row with `iloc[0]` (not with `loc[0]`, because the first row's label is
not `0`).


