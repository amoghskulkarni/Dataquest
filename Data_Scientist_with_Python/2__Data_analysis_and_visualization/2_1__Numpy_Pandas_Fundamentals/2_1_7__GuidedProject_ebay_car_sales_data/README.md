# 1. Introduction

<div><p>In this guided project, we'll work with a dataset of used cars from <em>eBay Kleinanzeigen</em>, a <a href="https://en.wikipedia.org/wiki/Classified_advertising" target="_blank">classifieds</a> section of the German eBay website.</p>
<p>The dataset was originally <a href="https://en.wikipedia.org/wiki/Web_scraping" target="_blank">scraped</a> and uploaded to Kaggle by user <a href="https://www.kaggle.com/orgesleka" target="_blank">orgesleka</a>.<br>
The original dataset isn't available on Kaggle anymore, but you can find it <a href="https://data.world/data-society/used-cars-data" target="_blank">here</a>.</p>
<p>We've made a few modifications from the original dataset:</p>
<ul>
<li>We sampled 50,000 data points from the full dataset, to ensure your code runs quickly in our hosted environment</li>
<li>We dirtied the dataset a bit to more closely resemble what you would expect from a scraped dataset (the version uploaded to Kaggle was cleaned to be easier to work with)</li>
</ul>
<p>The data dictionary provided with data is as follows:</p>
<ul>
<li><code>dateCrawled</code> - When this ad was first crawled. All field-values are taken from this date.</li>
<li><code>name</code> - Name of the car.</li>
<li><code>seller</code> - Whether the seller is private or a dealer.</li>
<li><code>offerType</code> - The type of listing</li>
<li><code>price</code> - The price on the ad to sell the car.</li>
<li><code>abtest</code> - Whether the listing is included in an A/B test.</li>
<li><code>vehicleType</code> - The vehicle Type.</li>
<li><code>yearOfRegistration</code> - The year in which the car was first registered.</li>
<li><code>gearbox</code> - The transmission type.</li>
<li><code>powerPS</code> - The power of the car in PS.</li>
<li><code>model</code> - The car model name.</li>
<li><code>kilometer</code> - How many kilometers the car has driven.</li>
<li><code>monthOfRegistration</code> - The month in which the car was first registered.</li>
<li><code>fuelType</code> - What type of fuel the car uses.</li>
<li><code>brand</code> - The brand of the car.</li>
<li><code>notRepairedDamage</code> - If the car has a damage which is not yet repaired.</li>
<li><code>dateCreated</code> - The date on which the eBay listing was created.</li>
<li><code>nrOfPictures</code> - The number of pictures in the ad.</li>
<li><code>postalCode</code> - The postal code for the location of the vehicle.</li>
<li><code>lastSeenOnline</code> - When the crawler saw this ad last online.</li>
</ul>
<p>The aim of this project is to clean the data and analyze the included used car listings. 
You'll also become familiar with some of the unique benefits jupyter notebook provides for pandas. </p>
<p>Let's start by importing the libraries we need and reading the dataset into pandas.</p></div>

### Instructions

<ul>
<li>Start by writing a paragraph in a markdown cell introducing the project and the dataset.</li>
<li>Import the pandas and NumPy libraries</li>
<li>Read the <code>autos.csv</code> CSV file into pandas, and assign it to the variable name <code>autos</code>.<ul>
<li>Try without specifying any encoding (which will default to <code>UTF-8</code>)</li>
<li>If you get an encoding error, try the next two most popular encodings (<code>Latin-1</code> and <code>Windows-1252</code>) until you are able to read the file without error.</li>
</ul>
</li>
<li>Create a new cell with just the variable <code>autos</code> and run this cell.<ul>
<li>A neat feature of jupyter notebook is its ability to render the first few and last few values of any pandas object.</li>
</ul>
</li>
<li>Use the <code>DataFrame.info()</code> and <code>DataFrame.head()</code> methods to print information about the <code>autos</code> dataframe, as well as the first few rows.<ul>
<li>Write a markdown cell briefly describing your observations.</li>
</ul>
</li>
</ul>

# 2. Cleaning column names 

<div><p>From the work we did in the last screen, we can make the following observations:</p>
<ul>
<li>The dataset contains 20 columns, most of which are strings.</li>
<li>Some columns have null values, but none have more than ~20% null values.</li>
<li>The column names use <a href="https://en.wikipedia.org/wiki/Camel_case" target="_blank">camelcase</a> instead of Python's preferred <a href="https://en.wikipedia.org/wiki/Snake_case" target="_blank">snakecase</a>, which means we can't just replace spaces with underscores.</li>
</ul>
<p>Let's convert the column names from camelcase to snakecase and reword some of the column names based on the data dictionary to be more descriptive.</p></div>

### Instructions 

<ul>
<li>Use the <code>DataFrame.columns</code> attribute to print an array of the existing column names.</li>
<li>Copy that array and make the following edits to columns names:<ul>
<li><code>yearOfRegistration</code> to <code>registration_year</code></li>
<li><code>monthOfRegistration</code> to <code>registration_month</code></li>
<li><code>notRepairedDamage</code> to <code>unrepaired_damage</code></li>
<li><code>dateCreated</code> to <code>ad_created</code></li>
<li>The rest of the column names from camelcase to snakecase.</li>
</ul>
</li>
<li>Assign the modified column names back to the <code>DataFrame.columns</code> attribute.</li>
<li>Use <code>DataFrame.head()</code> to look at the current state of the <code>autos</code> dataframe.</li>
<li>Write a markdown cell explaining the changes you made and why.</li>
</ul>

# 3. Initial exploration and cleaning 

<div><p>Now let's do some basic data exploration to determine what other cleaning tasks need to be done. Initially we will look for:</p>
<ul>
<li>Text columns where all or almost all values are the same.  These can often be dropped as they don't have useful information for analysis.</li>
<li>Examples of numeric data stored as text which can be cleaned and converted.</li>
</ul>
<p>The following methods are helpful for exploring the data:</p>
<ul>
<li><code>DataFrame.describe()</code> (with <code>include='all'</code> to get both categorical and numeric columns)</li>
<li><code>Series.value_counts()</code> and <code>Series.head()</code> if any columns need a closer look.</li>
</ul></div>

### Instructions 

<ul>
<li>Use <code>DataFrame.describe()</code> to look at descriptive statistics for all columns.</li>
<li>Write a markdown cell noting:<ul>
<li>Any columns that have mostly one value that are candidates to be dropped</li>
<li>Any columns that need more investigation.</li>
<li>Any examples of numeric data stored as text that needs to be cleaned.</li>
</ul>
</li>
<li>If you need to investigate any columns more, do so and write up any additional things you found.</li>
<li>You likely found that the <code>price</code> and <code>odometer</code> columns are numeric values stored as text.  For each column:<ul>
<li>Remove any non-numeric characters.</li>
<li>Convert the column to a numeric dtype.</li>
<li>Use <code>DataFrame.rename()</code> to rename the column to <code>odometer_km</code>.</li>
</ul>
</li>
</ul>

# 4. Exploring `odometer` and `price` columns 

<div><p>From the last screen, we learned that there are a number of text columns where almost all of the values are the same (<code>seller</code> and <code>offer_type</code>). We also converted the <code>price</code> and <code>odometer</code> columns to numeric types and renamed <code>odometer</code> to <code>odometer_km</code>.</p>
<p>Let's continue exploring the data, specifically looking for data that doesn't look right. We'll start by analyzing the <code>odometer_km</code> and <code>price</code> columns. Here's the steps we'll take:</p>
<ul>
<li>Analyze the columns using minimum and maximum values and look for any values that look unrealistically high or low (outliers) that we might want to remove.</li>
<li>We'll use:<ul>
<li><code>Series.unique().shape</code> to see how many unique values</li>
<li><code>Series.describe()</code> to view min/max/median/mean etc</li>
<li><code>Series.value_counts()</code>, with some variations:<ul>
<li>chained to <code>.head()</code> if there are lots of values.</li>
<li>Because <code>Series.value_counts()</code> returns a series, we can use <code>Series.sort_index()</code> with <code>ascending=</code> <code>True</code> or <code>False</code> to view the highest and lowest values with their counts (can also chain to <code>head()</code> here).</li>
</ul>
</li>
<li>When removing outliers, we can do <code>df[(df["col"] &gt;= x ) &amp; (df["col"] &lt;= y )]</code>, but it's more readable to use <code>df[df["col"].between(x,y)]</code></li>
</ul>
</li>
</ul></div>

### Instructions 

<ul>
<li>For each of the <code>odometer_km</code> and <code>price</code> columns:<ul>
<li>Use the techniques above to explore the data</li>
<li>If you find there are outliers, remove them and write a markdown paragraph explaining your decision.</li>
<li>After you have removed the outliers, make some observations about the remaining values.</li>
</ul>
</li>
</ul>

# 5. Exploring the columns that are date-type

<div><p>Let's now move on to the date columns and understand the date range the data covers.</p>
<p>There are 5 columns that should represent date values. Some of these columns were created by the crawler, some came from the website itself. We can differentiate by referring to the data dictionary:</p>
</div>

```
- `date_crawled`: added by the crawler
- `last_seen`: added by the crawler
- `ad_created`: from the website
- `registration_month`: from the website
- `registration_year`: from the website
```

<div>
<p>Right now, the <code>date_crawled</code>, <code>last_seen</code>, and <code>ad_created</code> columns are all identified as string values by pandas. Because these three columns are represented as strings, we need to convert the data into a numerical representation so we can understand it quantitatively. The other two columns are represented as numeric values, so we can use methods like <code>Series.describe()</code> to understand the distribution without any extra data processing.</p>
<p>Let's first understand how the values in the three string columns are formatted. These columns all represent full timestamp values, like so:</p>
</div>

```
autos[['date_crawled','ad_created','last_seen']][0:5]
```

<div>
<div>
<table>
<tbody><tr>
<th></th>
<th>date_crawled</th>
<th>ad_created</th>
<th>last_seen</th>
</tr>
<tr>
<td>0</td>
<td>2016-03-26 17:47:46</td>
<td>2016-03-26 00:00:00</td>
<td>2016-04-06 06:45:54</td>
</tr>
<tr>
<td>1</td>
<td>2016-04-04 13:38:56</td>
<td>2016-04-04 00:00:00</td>
<td>2016-04-06 14:45:08</td>
</tr>
<tr>
<td>2</td>
<td>2016-03-26 18:57:24</td>
<td>2016-03-26 00:00:00</td>
<td>2016-04-06 20:15:37</td>
</tr>
<tr>
<td>3</td>
<td>2016-03-12 16:58:10</td>
<td>2016-03-12 00:00:00</td>
<td>2016-03-15 03:16:28</td>
</tr>
<tr>
<td>4</td>
<td>2016-04-01 14:38:50</td>
<td>2016-04-01 00:00:00</td>
<td>2016-04-01 14:38:50</td>
</tr>
</tbody></table>
</div>
<p>You'll notice that the first 10 characters represent the day (e.g. <code>2016-03-12</code>). To understand the date range, we can extract just the date values, use <code>Series.value_counts()</code> to generate a distribution, and then sort by the index.</p>
<p>To select the first 10 characters in each column, we can use <code>Series.str[:10]</code>:</p>
</div>

```
print(autos['date_crawled'].str[:10])
```
```
0        2016-03-26
1        2016-04-04
2        2016-03-26
3        2016-03-12
...
```

### Instructions 

<ul>
<li>Use the workflow we just described to calculate the distribution of values in the <code>date_crawled</code>, <code>ad_created</code>, and <code>last_seen</code> columns (all string columns) as percentages.<ul>
<li>To include missing values in the distribution and to use percentages instead of counts, chain the <code>Series.value_counts(normalize=True, dropna=False)</code> method.</li>
<li>To rank by date in ascending order (earliest to latest), chain the <code>Series.sort_index()</code> method.</li>
<li>Write a markdown cell after each column exploration to explain your observations.</li>
</ul>
</li>
<li>Use <code>Series.describe()</code> to understand the distribution of <code>registration_year</code>.<ul>
<li>Write a markdown cell explaining your observations.</li>
</ul>
</li>
</ul>

# 6. Dealing with incorrect `registration_year` data

<div><p>One thing that stands out from the exploration we did in the last screen is that the <code>registration_year</code> column contains some odd values:</p>
<ul>
<li>The minimum value is <code>1000</code>, before cars were invented</li>
<li>The maximum value is <code>9999</code>, many years into the future</li>
</ul>
<p>Because a car can't be first registered after the listing was seen, any vehicle with a registration year above 2016 is definitely inaccurate. Determining the earliest valid year is more difficult. Realistically, it could be somewhere in the first few decades of the 1900s.</p>
<p>Let's count the number of listings with cars that fall outside the 1900 - 2016 interval and see if it's safe to remove those rows entirely, or if we need more custom logic.</p></div>

### Instructions 

<ul>
<li>Decide which the highest and lowest acceptable values are for the <code>registration_year</code> column.<ul>
<li>Write a markdown cell explaining your decision and why.</li>
</ul>
</li>
<li>Remove the values outside those upper and lower bounds and calculate the distribution of the remaining values using <code>Series.value_counts(normalize=True)</code>.<ul>
<li>Write a markdown cell explaining your observations.</li>
</ul>
</li>
</ul>

# 7. Exploring `price` by `brand`

<div><p>One of the analysis techniques we learned in this course is aggregation.  When working with data on cars, it's natural to explore variations across different car brands. We can use aggregation to understand the <code>brand</code> column.</p>
<p>If you recall in an earlier mission, we explored how to use loops to perform aggregation. Here's what the process looks like:</p>
<ul>
<li>Identify the unique values we want to aggregate by</li>
<li>Create an empty dictionary to store our aggregate data</li>
<li>Loop over the unique values, and for each:
        - Subset the dataframe by the unique values
        - Calculate the mean of whichever column we're interested in
        - Assign the val/mean to the dict as k/v.</li>
</ul></div>

### Instructions 

<ul>
<li>Explore the unique values in the <code>brand</code> column, and decide on which brands you want to aggregate by.  <ul>
<li>You might want to select the top 20, or you might want to select those that have over a certain percentage of the total values (e.g. &gt; 5%).</li>
<li>Remember that <code>Series.value_counts()</code> produces a series with index labels, so you can use <code>Series.index</code> attribute to access the labels, should you wish.</li>
</ul>
</li>
<li>Write a short paragraph describing the brand data, and explaining which brands you've chosen to aggregate on.</li>
<li>Create an empty dictionary to hold your aggregate data.<ul>
<li>Loop over your selected brands, and assign the mean price to the dictionary, with the brand name as the key.</li>
<li>Print your dictionary of aggregate data, and write a paragraph analyzing the results.</li>
</ul>
</li>
</ul>

# 8. Storing aggregate data in a DataFrame

<div><p>In the last screen, we aggregated across brands to understand mean price. We observed that in the top 6 brands, there's a distinct price gap.</p>
<ul>
<li>Audi, BMW and Mercedes Benz are more expensive</li>
<li>Ford and Opel are less expensive</li>
<li>Volkswagen is in between</li>
</ul>
<p>For the top 6 brands, let's use aggregation to understand the average mileage for those cars and if there's any visible link with mean price. While our natural instinct may be to display both aggregated series objects and visually compare them, this has a few limitations:</p>
<ul>
<li>it's difficult to compare more than two aggregate series objects if we want to extend to more columns</li>
<li>we can't compare more than a few rows from each series object</li>
<li>we can only sort by the index (brand name) of both series objects so we can easily make visual comparisons</li>
</ul>
<p>Instead, we can combine the data from both series objects into a single dataframe (with a shared index) and display the dataframe directly. To do this, we'll need to learn two pandas methods:</p>
<ul>
<li><a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html" target="_blank">pandas series constructor</a></li>
<li><a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html" target="_blank">pandas dataframe constructor</a></li>
</ul>
<p>Here's an example of the series constructor that uses the <code>brand_mean_prices</code> dictionary:</p>
</div>

```
bmp_series = pd.Series(brand_mean_prices)
print(bmp_series)
```
```
volkswagen       5402
bmw              8332
opel             2975
mercedes_benz    8628
audi             9336
ford             3749
dtype: int64
```

<div>
<p>The keys in the dictionary became the index in the series object. We can then create a single-column dataframe from this series object. We need to use the <code>columns</code> parameter when calling the dataframe constructor (which accepts an array-like object) to specify the column name (or the column name will be set to <code>0</code> by default):</p>
</div>

```
df = pd.DataFrame(bmp_series, columns=['mean_price'])
df
```

<div>
<div>
<table>
<tbody><tr>
<th></th>
<th>mean_price</th>
</tr>
<tr>
<td>volkswagen</td>
<td>5402</td>
</tr>
<tr>
<td>bmw</td>
<td>8332</td>
</tr>
<tr>
<td>opel</td>
<td>2975</td>
</tr>
<tr>
<td>mercedes_benz</td>
<td>8628</td>
</tr>
<tr>
<td>audi</td>
<td>9336</td>
</tr>
<tr>
<td>ford</td>
<td>3749</td>
</tr>
</tbody></table>
</div></div>

### Instructions 

<ul>
<li>Use the loop method from the last screen to calculate the mean mileage and mean price for each of the top brands, storing the results in a dictionary.</li>
<li>Convert both dictionaries to series objects, using the series constructor.</li>
<li>Create a dataframe from the first series object using the dataframe constructor.</li>
<li>Assign the other series as a new column in this dataframe.</li>
<li>Pretty print the dataframe, and write a paragraph analyzing the aggregate data.</li>
</ul>

# 9. Next steps 

<div><p>In this guided project, we practiced applying a variety of pandas methods to explore and understand a data set on car listings. Here are some next steps for you to consider:</p>
<ul>
<li>Data cleaning next steps:<ul>
<li>Identify categorical data that uses german words, translate them and map the values to their english counterparts</li>
<li>Convert the dates to be uniform numeric data, so <code>"2016-03-21"</code> becomes the integer <code>20160321</code>.</li>
<li>See if there are particular keywords in the name column that you can extract as new columns</li>
</ul>
</li>
<li>Analysis next steps:<ul>
<li>Find the most common brand/model combinations</li>
<li>Split the <code>odometer_km</code> into groups, and use aggregation to see if average prices follows any patterns based on the mileage.</li>
<li>How much cheaper are cars with damage than their non-damaged counterparts?</li>
</ul>
</li>
</ul>
<p>Curious to see what other students have done on this project? <a href="https://community.dataquest.io/tags/c/social/share/49/294" target="_blank">Head over to our Community to check them out</a>. While you are there, please remember to show some love and give your own feedback!</p>
<p>And of course, we welcome you to share your own project and show off your hard work. Head over to our Community to <a href="https://community.dataquest.io/tags/c/social/share/49/294" target="_blank">share your finished Guided Project</a>!</p></div>
