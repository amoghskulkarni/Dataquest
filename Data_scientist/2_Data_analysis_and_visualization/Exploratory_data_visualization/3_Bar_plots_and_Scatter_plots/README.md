# Data Scientist / Data Analysis and Visualization / Exploratory data visualization / Bar plots and Scatter plots

## Introduction 

Line charts were an appropriate choice for visualizing this dataset because the rows had a natural ordering to it. Each row reflected information about an event that occurred after the previous row. In this mission, we'll be working with a dataset that has no particular order.

## Intro To The Data

The dataset contains information about the reviews of 147 movies on Metacritic, Rotten Tomatoes and IMDB. The dataset also contains information about how many tickets got sold. 

The `fandango_scores.csv` file contains the following (and some other) columns:

- `FILM` - film name
- `RT_user_norm` - average user rating from Rotten Tomatoes, normalized to a 1 to 5 point scale
- `Metacritic_user_nom` - average user rating from Metacritc, normalized to a 1 to 5 point scale
- `IMDB_norm` - average user rating from IMDB, normalized to a 1 to 5 point scale
- `Fandango_Ratingvalue` - average user rating from Fandango, normalized to a 1 to 5 point scale
- `Fandango_Stars` - the rating displayed on the Fandango website (rounded to nearest star, 1 to 5 point scale)

Instead of displaying the raw rating, the writer discovered that Fandango usually rounded the average rating to the next highest half star (next highest `0.5` value). The `Fandango_Ratingvalue` column reflects the true average rating while the `Fandango_Stars` column reflects the displayed, rounded rating.

## Bar Plot

The `RT_user_norm`, `Metacritic_user_nom`, `IMDB_norm`, and `Fandango_Ratingvalue` columns contain the average user rating for each movie, normalized to a `0` to `5` point scale. While calculating and comparing summary statistics give us hard numbers for quantifying the bias, visualizing the data using plots can help us gain a more intuitive understanding. We need a visualization that scales graphical objects to the quantitative values we're interested in comparing. One of these visualizations is a **bar plot**.

## Creating Bars

When we generated line charts, we passed in the data to `pyplot.plot()` and matplotlib took care of the rest. Because the markers and lines in a line chart correspond directly with x-axis and y-axis coordinates, all matplotlib needed was the data we wanted plotted. To create a useful bar plot, however, we need to specify the positions of the bars, the widths of the bars, and the positions of the axis labels. Here's a diagram that shows the various values we need to specify:

![Alt text](/matplotlib_barplot_positioning.png?raw=true "Optional Title")

[`pyplot.subplot()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots) can be used to generate a single subplot and figure object, and can replace the following code snippet -

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Equivalent to
fig, ax = plt.subplots()
```

We can generate a vertical bar plot using either [`pyplot.bar()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar) or [`Axes.bar()`](http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar). 

The method has 2 required parameters, `left` and `height`. We use the `left` parameter to specify the x coordinates of the left sides of the bar (marked in blue on the above image). We use the `height` parameter to specify the height of each bar. Both of these parameters accept a list-like object. 

```python
bar_positions = arange(5) + 0.75

bar_heights = norm_reviews[num_cols].iloc[0].values
```

P.S. [`arange()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html) works like `range()`.

We can also use the `width` parameter to specify the width of each bar (also a list-like object).

## 
