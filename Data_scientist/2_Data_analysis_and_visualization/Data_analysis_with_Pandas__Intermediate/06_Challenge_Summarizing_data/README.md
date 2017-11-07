# Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Challenge: Summarizing data

## 1. Introduction to the Data

-----

Some of the total of `21` columns in both the files, `recent-grads.csv` as well as `all-ages.csv` -

`Rank` - The major's numerical rank, by post-graduation median earnings  
`Major_code` - The major's numerical code  
`Major` - The major's description  
`Major_category` - The major's category  
`Total` - The total number of people who studied the major  
`Sample_size` - Sample size (unweighted) of full-time, year-round students  
`Men` - The number of men who studied the major  
`Women` - The number of women who studied the major  
`ShareWomen` - The share of women (from `0` to `1`) who studied the major  
`Employed` - The number of people who studied the major and obtained a job after graduating  
`Low_wage_jobs` - Number in low-wage service jobs  

Instructions -

- Read `all-ages.csv` into a DataFrame object, and assign it to `all_ages`.
- Read `recent-grads.csv` into a DataFrame object, and assign it to `recent_grads`.
- Display the first five rows of `all_ages` and `recent_grads`.

```python
import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages.head(5))
print(recent_grads.head(5))

print(all_ages.loc[0:5])                # This also works
```

## 2. Summarizing Major Categories

-----

Both of these data sets group the various majors into categories in the `Major_category` column. 
Let's start by understanding the number of people in each `Major_category` for both data sets.

The `Series` object has a method named `unique()` which gives unique elements in the series. Example of 
[`Series.unique()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.unique.html) -

```python
print(all_ages['Major_category'].unique())
```

To find out the rows from the original dataframe that take those unique values -

```python
for u in df['Major_category'].unique():
    df_of_particular_u = df[ df["Major_category"] == u ]
```

The result of `df['Major_category'].unique()` is a list, but `df[ df["Major_category"] == u ]` is a df.
So all the other functions of `DataFrame` can be used on that result.

In this example we sum up a column named `Total` from the resultant df.

```python
    total = major_df["Total"].sum()
```

Final solution -

```python
# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum()
        counts_dictionary[c] = total

    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)
```

## 3. Low-Wage Job Rates

-----

### Instructions

- Use the `Low_wage_jobs` and `Total` columns to calculate the proportion of recent college graduates that worked low wage jobs.
  - Recall that you can use the [`Series.sum()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sum.html) method to return the sum of the values in a column.
- Store the resulting _float_ as `low_wage_proportion,` and display the value with the `print()` function.

```python
total_jobs = recent_grads["Total"].sum()
low_wage_jobs = recent_grads["Low_wage_jobs"].sum()

low_wage_proportion = float(low_wage_jobs) / float(total_jobs)

print(low_wage_proportion)
```

## 5. Comparing Data Sets

-----

Both the `all_ages` and `recent_grads` data sets have 173 rows, corresponding to the 173 college major codes. Perform some initial calculations to see how the statistics for recent college graduates compare with those for the entire population.

### Instructions

- Use a `for` loop to iterate over `majors`.
  - For each major, compare the values for `Unemployment_rate` to see which DataFrame has a lower value.
  - Increment `rg_lower_count` if the value for `Unemployment_rate` is lower for `recent_grads` than it is for `all_ages`.
- Display `rg_lower_count`.

P.S. Here, we have `recent_grads['Major'].unique()` stored in the variable `majors`. 

Answer - 

```python
for major in majors:
    rg_major = recent_grads[ recent_grads["Major"] == major ]
    aa_major = all_ages[ all_ages["Major"] == major ]
    
    ue_rg_major = float(rg_major["Unemployment_rate"])
    ue_aa_major = float(aa_major["Unemployment_rate"])
        
    if ue_rg_major < ue_aa_major:
        rg_lower_count += 1

print(rg_lower_count)
```