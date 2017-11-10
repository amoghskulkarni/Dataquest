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

## Table Representation

-----

The dataset contains 2 columns:

- `DATE`: date, always the first of the month. Here are some examples:
  - `1948-01-01`: January 1, 1948.
  - `1948-02-01`: February 1, 1948.
  - `1948-03-01`: March 1, 1948.
  - `1948-12-01`: December 1, 1948.
- `VALUE`: the corresponding unemployment rate, in percent.

## Observations From The Table Representation

-----

Because the table only contained the data from 1948, it didn't take too much time to identify these observations. If we scale up the table to include all 824 rows, it would be very time-consuming and painful to understand. Tables shine at presenting information precisely at the intersection of rows and columns and allow us to perform quick lookups when we know the row and column we're interested in. Unfortunately, many problems you'll encounter in data science require comparisons that aren't possible with just tables.

## Visual Representation

-----

Different types of plots, line charts being one of them. Importance and uses.

## Introduction to Matplotlib

-----

To create the line chart, we'll use the matplotlib library.

When working with commonly used plots in matplotlib, the general workflow is:

- create a plot using data
  - `plt.plot()`
- customize the appearance of the plot
- display the plot
  - `plt.show()`
- edit and repeat until satisfied

We didn't assign the plot to a variable and then call a method on the variable to display it. We instead called 2 functions on the pyplot module directly.This is because every time we call a pyplot function, the module maintains and updates the plot internally (also known as state). When we call `show()`, the plot is displayed and the internal state is destroyed.

## Adding Data

-----

We can just specify the data we want plotted and let matplotlib handle the rest. To generate the line chart we're interested in, we pass in the list of x-values as the first parameter and the list of y-values as the second parameter to `plot()`:

```python
plt.plot(x_values, y_values)
```

# Fixing Axis Ticks

-----

While the y-axis looks fine, the x-axis tick labels are too close together and are unreadable. The line charts from earlier in the mission suggest a better way to display the x-axis tick labels. We can rotate the x-axis tick labels by 90 degrees so they don't overlap. The [`xticks()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xticks) function within pyplot lets you customize the behavior of the x-axis ticks. There's a `rotation` parameter that accepts degrees of rotation as a parameter.

```python
# Example
xticks( arange(12), calendar.month_name[1:13], rotation=17 )
```

## Adding Axis Labels And A Title

-----

- [`xlabel()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlabel): accepts a string value, which gets set as the x-axis label.
- [`ylabel()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylabel): accepts a string value, which is set as the y-axis label.
- [`title()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.title): accepts a string value, which is set as the plot title.
