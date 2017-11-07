Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Data Manipulation with pandas
==========================================================================================================================

1. Overview
-----------

We'll continue to work with the same data set from the USDA on nutritional information. We'll build a basic nutritional 
index for people who want to eat high-protein, low-fat foods. The `Lipid_Tot_(g)` column contains each food's total fat 
content, and the `Protein_(g)` (in grams) contains each food's total protein content (in grams). Let's use the following 
formula to score each food in our data set:

```python
score = 2 * (Protein_(g)) − 0.75 * (Lipid_Tot_(g))
```

For reviewing what we learnt in the last lesson, let's
- Read the file (`pandas.read_csv()`)
- Column names (`Series.tolist()`)
- Print first n rows (`DataFrame.head(n)`)

```python
import pandas
food_info = pandas.read_csv("food_info.csv")
col_names = food_info.columns.tolist()
print(col_names)
print(food_info.head(3))
```

2. Transforming a column
------------------------

Mathematical operators can be applied on `Series` objects like the ones returned by `DataFrame.column`. 

```python
iron_mg = food_info["Iron_(mg)"]                # iron_mg is a Series object
```

You can transform a column by using mathematical operators like addition, subtraction etc. which returns
a `Series` object just like the one returned in the above cell. The operation is carried out on every element
of the original `Series` object.

```python
div_1000 = food_info["Iron_(mg)"] / 1000
```

Some more examples are -

```python
# Adds 100 to each value in the column and returns a Series object.
add_100 = food_info["Iron_(mg)"] + 100

# Subtracts 100 from each value in the column and returns a Series object.
sub_100 = food_info["Iron_(mg)"] - 100

# Multiplies each value in the column by 2 and returns a Series object.
mult_2 = food_info["Iron_(mg)"]*2
```

3. Performing math with multiple columns
----------------------------------------

`Series` objects can be operated on by mathematical operators with scalars as well as other `Series` object.
I.e. two columns in a `DataFrame` can be added, subtracted etc. _element by element_. 

```python
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
```

The object returned is a `Series` object.

4. Create a nutritional index
-----------------------------

The formula is - `Score = 2*(Protein_(g)) − 0.75*(Lipid_Tot_(g))`

```python
weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = food_info["Lipid_Tot_(g)"] * -0.75
initial_rating = weighted_protein + weighted_fat
```

5. Normalising columns in a dataset
-----------------------------------

The columns in the data set use different units (kilo-calories, milligrams, etc.). As a result, the range 
of values varies greatly between columns. For example, the `Vit_A_IU` column ranges from 0 to 100000, while 
the `Fiber_TD_(g)` column ranges from 0 to 79. For certain calculations, columns like `Vit_A_IU` can have 
a greater effect on the result, due to the scale of the values.

While there are many ways to normalize data, one of the simplest ways is to divide all of the values in 
a column by that column's maximum value.

```python
# The largest value in the "Energ_Kcal" column.
max_calories = food_info["Energ_Kcal"].max()

# Divide the values in "Energ_Kcal" by the largest value.
normalized_calories = food_info["Energ_Kcal"] / max_calories
```

6. Creating a new column
------------------------

Assigning the `Series` object to a column in `DataFrame` creates a new column in the `DataFrame`.

```python
food_info["Iron_(g)"] = food_info["Iron_(mg)"] / 1000
```

7. Create a normalized nutritional index
----------------------------------------

```python
food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

food_info["Norm_Nutr_Index"] = 2 * food_info["Normalized_Protein"] - 0.75 * food_info["Normalized_Fat"]
```

8. Sorting a `DataFrame` by a column
------------------------------------

The `DataFrame` can be sorted with respect to the values of a particular column. There are multiple possible
options in the sorting operation, but two of the most useful are -

- `inplace`  
Setting this to `True` or `False` will change whether the same `DataFrame` is changed or a separate `DataFrame`
is returned. If set to `True`, the same `DataFrame` is changed. By default it is set to `False`, which causes
the method to return a new `DataFrame`.

- `ascending`  
Fairly self explanatory.

