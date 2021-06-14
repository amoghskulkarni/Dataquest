# Introduction: The I-94 Traffic Dataset

<div><p>At the beginning of the course, we saw that there are two types of data visualization:</p>
<ul>
<li>Exploratory data visualization: we build graphs for <em>ourselves</em> to explore data and find patterns.</li>
<li>Explanatory data visualization: we build graphs for <em>others</em> to communicate and explain the patterns we've found through exploring data.</li>
</ul>
<p></p><center><img src="https://s3.amazonaws.com/dq-content/520/exploratory_explanatory.svg" alt="img"></center><p></p>
<p>Throughout this course, we focused only on exploratory data visualization and learned the following:</p>
<ul>
<li>How to visualize time series data with line plots.</li>
<li>How to visualize correlations with scatter plots.</li>
<li>How to visualize frequency distributions with bar plots and histograms.</li>
<li>How to speed up our exploratory data visualization workflow with the pandas library.</li>
<li>How to compare graphs using grid charts.</li>
</ul>
<p>To make learning smoother and more efficient, we learned about each of these topics in isolation. In this guided project, we'll go one step further and learn to combine these skills.</p>
<p>We're going to analyze a dataset about the westbound traffic on the <a href="https://en.wikipedia.org/wiki/Interstate_94" target="_blank">I-94 Interstate highway</a>.</p>
<p>John Hogue made the dataset available, and you can download it from the <a href="https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume" target="_blank">UCI Machine Learning Repository</a>.</p>
<p>The goal of our analysis is to determine a few indicators of heavy traffic on I-94. These indicators can be weather type, time of the day, time of the week, etc. For instance, we may find out that the traffic is usually heavier in the summer or when it snows.</p>
<p>You can find the solution notebook <a href="https://github.com/dataquestio/solutions/blob/master/Mission524Solutions.ipynb" target="_blank">at this link</a>. Let's start!</p></div>

### Instructions 

<ol>
<li>To help readers gain context into your project, use the first Markdown cell of the notebook to do the following:<ul>
<li>Add a title.</li>
<li>Write a short introduction that explains the following in no more than two paragraphs:<ul>
<li>What the project is about</li>
<li>Your goal with this project</li>
</ul>
</li>
<li>Side note: the title and the introduction are tentative at this point — you can come back at the end of your work to change them.</li>
</ul>
</li>
<li>Read in the <code>Metro_Interstate_Traffic_Volume.csv</code> file using Pandas.</li>
<li>Examine the first and the last five rows.</li>
<li>Use <code>DataFrame.info()</code> to find more information about the dataset.</li>
</ol>

# Analyzing Traffic Volume

<div><p>On the previous screen, we read in the dataset and set our analysis goal: determine indicators of heavy traffic on I-94.</p>
<p>The <a href="https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume" target="_blank">dataset documentation</a> mentions that a station located approximately midway between Minneapolis and Saint Paul recorded the traffic data. Also, the station only records westbound traffic (cars moving from east to west).</p>
<p></p><center><img src="https://s3.amazonaws.com/dq-content/524/i94_figma.png" alt="img"></center><p></p>
<p>This means that the results of our analysis will be about the westbound traffic in the proximity of that station. In other words, we should avoid generalizing our results for the entire I-94 highway.</p>
<p>In the next exercise, we're going to plot a histogram to visualize the distribution of the <code>traffic_volume</code> column. </p>
<p>When we use Matplotlib inside Jupyter, we also need to add the <code>%matplotlib inline</code> magic — this enables Jupyter to generate the graphs.</p>
</div>

```
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot()
plt.show()
```

<div>
<p>We only need to run <code>%matplotlib inline</code> once inside a notebook. If we have a notebook with ten cells, and we plot a graph in each cell, it's enough to add <code>%matplotlib inline</code> in the first cell.</p></div>

# Traffic volume: Day vs. Night

<div><p>Previously, we analyzed the distribution of <code>traffic_volume</code> and found the following:</p>
<ul>
<li>About 25% of the time, there were 1,193 cars or fewer passing the station each hour — this probably occurs during the night, or when a road is under construction.</li>
<li>About 25% of the time, the traffic volume was four times as much (4,933 cars or more).</li>
</ul>
<p>This possibility that nighttime and daytime might influence traffic volume gives our analysis an interesting direction: comparing daytime with nighttime data.</p>
<p>We'll start by dividing the dataset into two parts:</p>
<ul>
<li>Daytime data: hours from 7 a.m. to 7 p.m. (12 hours)</li>
<li>Nighttime data: hours from 7 p.m. to 7 a.m. (12 hours)</li>
</ul>
<p>While this is not a perfect criterion for distinguishing between nighttime and daytime, it's a good starting point.</p></div>

### Instructions 

<ol>
<li>Transform the <code>date_time</code> column to <code>datetime</code> by using the function <code>pd.to_datetime()</code>.</li>
<li>Use the <code>Series.dt.hour</code> property to get the hour of every instance of the <code>date_time</code> column and do the following:<ul>
<li>Isolate the daytime data.</li>
<li>Isolate the nighttime data.</li>
</ul>
</li>
</ol>

# Traffic volume: Day vs. Night (II)

<div><p>Previously, we divided the dataset into two parts:</p>
<ul>
<li>Daytime data: hours from 7 AM to 7 PM (12 hours)</li>
<li>Nighttime data: hours from 7 PM to 7 AM (12 hours)</li>
</ul>
<p>Now we're going to compare the traffic volume at night and during day.</p></div>

### Instructions 
<ol>
<li>Plot the histograms of <code>traffic_volume</code> for both day and night. Organize the two histograms side-by-side on a grid chart.</li>
<li>For both histograms, do the following:<ul>
<li>Add a title.</li>
<li>Add x- and y-labels.</li>
<li>Bring the x- and the y-axis to the same ranges (this will help you compare the histograms correctly).</li>
</ul>
</li>
<li>Use <code>Series.describe()</code> to look up a few statistics for <code>traffic_volume</code> for both day and night.</li>
<li>Analyze the results:<ul>
<li>What shape do the histograms have and what does that indicate?</li>
<li>If the traffic is light at night, and our goal is to find indicators of heavy traffic, should we still be using the nighttime data?</li>
</ul>
</li>
</ol>

# Time indicators 

<div><p>Previously, we determined that the traffic at night is generally light. Our goal is to find indicators of heavy traffic, so we decided to only focus on the daytime data moving forward.</p>
<p>One of the possible indicators of heavy traffic is time. There might be more people on the road in a certain month, on a certain day, or at a certain time of the day.</p>
<p>We're going to look at a few line plots showing how the traffic volume changed according to the following parameters:</p>
<ul>
<li>Month</li>
<li>Day of the week</li>
<li>Time of day</li>
</ul>
<p>The fastest way to get the average traffic volume for each month is by using the <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html" target="_blank"><code>DataFrame.groupby()</code> method</a>. If you haven't yet learned this method, don't worry: we'll write out the code for you, and you'll only have to focus on the visualization code.</p>
<p>In the code below, we'll do the following:</p>
<ul>
<li>Use <code>day['date_time'].dt.month</code> to create a new column where each value describes the month when the traffic volume measurement was taken.</li>
<li>Use <code>day.groupby('month').mean()</code> to group the dataset by the <code>month</code> column with the mean as an aggregate function.</li>
</ul>
</div>

```
day['month'] = day['date_time'].dt.month
by_month = day.groupby('month').mean()
by_month['traffic_volume']
```
```
month
1     4495.613727
2     4711.198394
3     4889.409560
4     4906.894305
5     4911.121609
6     4898.019566
7     4595.035744
8     4928.302035
9     4870.783145
10    4921.234922
11    4704.094319
12    4374.834566
Name: traffic_volume, dtype: float64
```

<div>
<p>Let's start with generating the plot for the first time unit mentioned above — the month.</p></div>

### Instructions 

<ol>
<li>Copy the code above and run it into your notebook to get the monthly traffic volume averages.</li>
<li>Generate a line plot to visualize how the traffic volume changed each month on average.</li>
<li>Analyze the line plot. Do you notice any interesting exception?</li>
</ol>

# Time indicators (II)

<div><p>In the previous screen, we generated a line plot showing how the traffic volume changed each month on average.</p>
<p>We'll now continue with building line plots for another time unit: day of the week.</p>
<p>To get the traffic volume averages for each day of the week, we'll need to use the following code:</p>
</div>

```
day['dayofweek'] = day['date_time'].dt.dayofweek
by_dayofweek = day.groupby('dayofweek').mean()
by_dayofweek['traffic_volume']  # 0 is Monday, 6 is Sunday
```
```
dayofweek
0    4893.551286
1    5189.004782
2    5284.454282
3    5311.303730
4    5291.600829
5    3927.249558
6    3436.541789
Name: traffic_volume, dtype: float64
```

### Instructions 

# Time indicators (III)

<div><p>On the previous screen, we found that the traffic volume is significantly heavier on business days compared to the weekends.</p>
<p>We'll now generate a line plot for the time of day. The weekends, however, will drag down the average values, so we're going to look at the averages separately. To do that, we'll start by splitting the data based on the day type: business day or weekend.</p>
<p>Below, we show you how to split the dataset so you can focus on plotting the graphs. While your variable names may vary, the logic of the code should be the same.</p>
</div>

```
day['hour'] = day['date_time'].dt.hour
bussiness_days = day.copy()[day['dayofweek'] <= 4] # 4 == Friday
weekend = day.copy()[day['dayofweek'] >= 5] # 5 == Saturday
by_hour_business = bussiness_days.groupby('hour').mean()
by_hour_weekend = weekend.groupby('hour').mean()

print(by_hour_business['traffic_volume'])
print(by_hour_weekend['traffic_volume'])
```
```
hour
7     6030.413559
8     5503.497970
9     4895.269257
10    4378.419118
11    4633.419470
12    4855.382143
13    4859.180473
14    5152.995778
15    5592.897768
16    6189.473647
17    5784.827133
18    4434.209431
Name: traffic_volume, dtype: float64

hour
7     1589.365894
8     2338.578073
9     3111.623917
10    3686.632302
11    4044.154955
12    4372.482883
13    4362.296564
14    4358.543796
15    4342.456881
16    4339.693805
17    4151.919929
18    3811.792279
Name: traffic_volume, dtype: float64
```

### Instructions 

<ol>
<li>Plot two line plots on a grid chart to visualize how the traffic volume changes by time of the day.<ul>
<li>One plot shows how traffic volume changes during business days and the other shows how it changes during weekends.</li>
<li>Add a title to each graph.</li>
<li>Bring both graphs to the same x- and y-axis range.</li>
</ul>
</li>
<li>Analyze both charts. How do they compare? When are the rush hours on business days?</li>
<li>Summarize all your findings regarding time indicators for heavy traffic.</li>
</ol>

# Weather indicators 

<div><p>So far, we've focused on finding time indicators for heavy traffic, and we reached the following conclusions:</p>
<ul>
<li>The traffic is usually heavier during warm months (March–October) compared to cold months (November–February).</li>
<li>The traffic is usually heavier on business days compared to weekends.</li>
<li>On business days, the rush hours are around 7 and 16.</li>
</ul>
<p>Another possible indicator of heavy traffic is weather. The dataset provides us with a few useful columns about weather: <code>temp</code>, <code>rain_1h</code>, <code>snow_1h</code>, <code>clouds_all</code>, <code>weather_main</code>, <code>weather_description</code>.</p>
<p>A few of these columns are numerical so let's start by looking up their correlation values with <code>traffic_volume</code>.</p></div>

### Instructions 

<ol>
<li>Find the correlation values between <code>traffic_volume</code> and the numerical weather columns.</li>
<li>Find the weather column with the strongest correlation with <code>traffic_volume</code> and plot a scatter plot for this weather column and <code>traffic_volume</code>.</li>
<li>Do any of these weather columns seem like reliable indicators for heavy traffic?</li>
</ol>

# Weather types 

<div><p>Previously, we examined the correlation between <code>traffic_volume</code> and the numerical weather columns. However, we didn't find any reliable indicator of heavy traffic.</p>
<p>To see if we can find more useful data, we'll look next at the categorical weather-related columns: <code>weather_main</code> and <code>weather_description</code>.</p>
<p>We're going to calculate the average traffic volume associated with each unique value in these two columns. We've already calculated the values for you — we grouped the data by <code>weather_main</code> and <code>weather_description</code> while using the mean as an aggregate function.</p>
</div>

```
by_weather_main = day.groupby('weather_main').mean()
by_weather_description = day.groupby('weather_description').mean()
```

<div>
<p>Let's create a bar plot for the <code>traffic_volume</code> column of <code>by_weather_main</code> and <code>by_weather_description</code>.</p></div>  

### Instructions 

<ol>
<li>Plot a horizontal bar plot for the <code>traffic_volume</code> column of <code>by_weather_main</code>.</li>
<li>Analyze the bar plot. Is there any traffic volume exceeding 5,000 cars? Can you find any weather type as a heavy traffic indicator?</li>
<li>Plot a horizontal bar plot for the <code>traffic_volume</code> column of <code>by_weather_description</code>. This column has many unique values, so you'll need to enlarge the figure size to make it readable. You can use <code>plt.figure(figsize=(width,height))</code> or <code>Series.plot.barh(figsize=(width,height))</code>.</li>
<li>Analyze the bar plot. Is there any traffic volume exceeding 5,000 cars? Can you find any weather type as a heavy traffic indicator?</li>
<li>Write up your conclusions for the entire project — this was the last step.</li>
</ol>

<div><p>In this project, we tried to find a few indicators of heavy traffic on the I-94 Interstate highway. We managed to find two types of indicators:</p>
<ul>
<li>Time indicators<ul>
<li>The traffic is usually heavier during warm months (March–October) compared to cold months (November–February).</li>
<li>The traffic is usually heavier on business days compared to the weekends.</li>
<li>On business days, the rush hours are around 7 and 16.</li>
</ul>
</li>
<li>Weather indicators<ul>
<li>Shower snow</li>
<li>Light rain and snow</li>
<li>Proximity thunderstorm with drizzle</li>
</ul>
</li>
</ul>
<p>Next steps include the following:</p>
<ul>
<li>Use the nighttime data to look for heavy traffic indicators.</li>
<li>Find more time and weather indicators.</li>
<li>Make your project portfolio-ready by following this <a href="https://www.dataquest.io/blog/data-science-project-style-guide/" target="_blank">style guide</a>.</li>
</ul>
<p>Curious to see what other students have done on this project? <a href="https://community.dataquest.io/tags/c/social/share/49/524" target="_blank">Head over to our Community to check them out</a>. While you are there, please share your own feedback!</p>
<p>And of course, we welcome you to share your own project and show off your hard work. Head over to our Community to <a href="https://community.dataquest.io/tags/c/social/share/49/524" target="_blank">share your finished Guided Project</a>!</p></div>