Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Challenge: Summarizing data
========================================================================================================================

1. Introduction to the Data
---------------------------

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

2. Summarizing Major Categories
-------------------------------
