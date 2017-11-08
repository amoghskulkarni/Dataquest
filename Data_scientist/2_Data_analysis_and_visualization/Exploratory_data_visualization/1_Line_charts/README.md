# Data Scientist / Data Analysis and Visualization / Exploratory data visualization / Line charts

## Representation Of Data

-----

Tables bad, plots good, Blah blah.

## Introduction To The Data

-----

United States Bureau of Labor Statistics (BLS) releases monthly unemployment data. The monthly unemployment rate as a CSV from January 1948 to August 2016, saved as `unrate.csv`, is available in this mission. The dataset we'll be working with is a time series dataset, which means the data points (monthly unemployment rates) are ordered by time. Here's a preview of the dataset:

**DATE** | **VALUE**
:---:|:---:
1948-01-01|3.4
1948-02-01|3.8
1948-03-01|4.0

When we read the dataset into a DataFrame, pandas will set the data type of the `DATE` column as a text column. Because of how pandas reads in strings internally, this column is given a data type of `object`. We need to convert this column to the `datetime` type using the [`pandas.to_datetime()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) function, which returns a Series object with the datetime data type that we can assign back to the DataFrame:

```python
import pandas as pd
df['col'] = pd.to_datetime(df['col'])
```


