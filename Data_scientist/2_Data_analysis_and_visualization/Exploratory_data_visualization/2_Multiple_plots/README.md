# Data Scientist / Data Analysis and Visualization / Exploratory data visualization / Multiple Plots

## Recap

-----

Blah.

## Matplotlib Classes

-----

When we were working with a single plot, pyplot was storing and updating the state of that single plot. When we want to work with multiple plots, however, we need to be more explicit about which plot we're making changes to.

Let's first start by understanding what pyplot was automatically storing under the hood when we create a single plot:

- **a container for all plots was created (returned as a [`Figure`](http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure) object)**
  
  A figure acts as a container for all of our plots and has methods for customizing the appearance and behavior for the plots within that container. 

- **a container for the plot was positioned on a grid (the plot returned as an [`Axes`](http://matplotlib.org/api/axes_api.html#matplotlib-axes) object)**
  
  After a figure is created, an axes for a single plot containing no data is created within the context of the figure.
  
  The Axes object acts as its own container for the various components of the plot, such as:

  - values on the x-axis and y-axis
  - ticks on the x-axis and y-axis
  - all visual symbols, such as:
    - markers
    - lines
    - gridlines

- **visual symbols were added to the plot (using the Axes methods)**

While plots are represented using instances of the Axes class, they're also often referred to as subplots in matplotlib. [`Figure.add_subplot`](http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.add_subplot) will return a new `Axes` object, which needs to be assigned to a variable:

```python
axes_obj = fig.add_subplot(nrows, ncols, plot_number)
```

If we want the figure to contain 2 plots, one above the other, we need to write:

```python
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
```

First parameter to the method is number of *rows* and the second one is number of *columns* in the grid to be created.

This will create a grid, `2` rows by `1` column, of plots. The first call to `add_subplot()` will render the returned `Axes` object (`ax1`) in the first position (top), the second call will render the returned `Axes` object in the second position (bottom). The numbering is from left to right, top to bottom in case of 2D grid. 

## Grid Positioning

-----

Some more trivial info about the method and its parameters. Nothing to be noted separately.

## Adding Data

-----

To generate a line chart within an Axes object, we need to call `Axes.plot()` and pass in the data you want plotted much like the way `plt.plot()` was used.

```python
ax1 = fig.add_subplot(2, 1, 1)
x_values = [0.0, 0.5, 1.0]
y_values = [10, 20, 40]
ax1.plot(x_values, y_values)
```

## Formatting And Spacing

-----

One issue with the 2 plots is that the x-axis ticks labels are unreadable. If we want to expand the plotting area, we have to specify this ourselves when we create the figure. To tweak the dimensions of the plotting area, we need to use the `figsize` parameter when we call `plt.figure()`:

```python
fig = plt.figure(figsize=(width, height))
```

The unit for both width and height values is inches. The `dpi` parameter, or dots per inch, and the `figsize` parameter determine how much space on your display a plot takes up.

## Comparing Across More Years

-----

Let's visualize data from a few more years to see if we find any evidence for seasonality between those years.

## Overlaying Line Charts

-----

By adding more line charts, we can look across more years for seasonal trends, but we now have to visually scan over more space, which is a limitation that we experienced when scanning the table representation of the same data. We can handle the visual overhead each additional plot adds by overlaying the line charts in a single subplot.