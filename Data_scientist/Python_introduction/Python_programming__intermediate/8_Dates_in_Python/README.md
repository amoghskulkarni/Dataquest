Data Scientist / Python Introduction / Python Programming: Intermediate / Dates in Python
=========================================================================================

1. The `time` module
--------------------

`time` module has a `time()` function which returns the Unix-style time value which represents
no. of seconds passed since the 'epoch' (first second of 1970). The `time` module also has other
handy functions.

```python
import time
current_time = time.time()          # Prints human-unfriendly float value of the timestamp
``` 

2. Converting timestamp
-----------------------

The `gmtime()` function takes a timestamp as an argument, and returns an instance of the 
`struct_time` class.

Each `struct_time` instance has some properties that represent the current time. 
The following integer values are just a few of these properties:

- `tm_year`: The year of the timestamp
- `tm_mon`: The month of the timestamp (1-12)
- `tm_mday`: The day in the month of the timestamp (1-31)
- `tm_hour`: The hour of the timestamp (0-23)
- `tm_min`: The minute of the timestamp (0-59)

```python
current_time = time.time()

current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
```

3. UTC
------

The `time` module deals primarily with timestamps in **UTC**. The `datetime` module has better 
support for working extensively with dates. With `datetime`, it is easier to work with different 
time zones and perform arithmetic (adding days, for example) on dates.

`datetime` module has a class called `datetime` which has most of the methods required to process
dates and times worldwide. `datetime` is similar to `struct_time` and has the fields `year`, `month`,
`day`, `hour`, `minute`, `second` and `microsecond`. 

The `datetime` class from the module doesn't need to be instantiated in order to use its methods. 

```python
import datetime
current_datetime = datetime.datetime.now()

current_year = current_datetime.year
current_month = current_datetime.month
```

4. Timedelta
------------

Since adding a day, week, month, etc. to a date can be tedious to do from scratch, the `datetime` module
provides the `timedelta` class. We can create an instance of the `timedelta` class that represents 
a span of time.

```python
today = datetime.datetime.now()
diff = datetime.timedelta(weeks=3, days=2)
result = today + diff
```

Another example -

```python
today = datetime.datetime.now()
diff = datetime.timedelta(days=1)
tomorrow = today + diff
yesterday = today - diff
```

5. Formatting dates
-------------------

If we print `datetime` object, it'll look something like `2016-01-06 13:51:25.849719`. The `datetime`
class provides `strftime()` method to format the time.

[strftime() documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
will provide the further information about formatting options.

```python
march3 = datetime.datetime(year = 2010, month = 3, day = 3)
pretty_march3 = march3.strftime("%b %d, %Y")
print(pretty_march3)            # March 3, 2010
```

6. Parsing dates
----------------

`strptime()` method of `datetime` class can be used to convert string to `datetime` object. It accepts
formatting string and the string to be parsed.

The following code will store appropriate `datetime` object in `march3` - 

```python
march3 = datetime.datetime.strptime("Mar 03, 2010", "%b %d, %Y")
```

7. Dataset: AskReddit data
--------------------------

1000 datapoints of top 1000 Reddit posts of 2015, each row datapoint containing -

Field | Description
:---: | :----:
Title | The title of the post
Score | The number of upvotes the post received
Time | When the post was posted
Gold | How much Reddit Gold was given to the post
NumComs | Number of comments the post received

8. Reformatting our data
------------------------

Store the time in each datapoint in the form of `datetime` instance. Use `fromtimestamp()` method
of `datetime` class.

```python
for post in posts:
    post[2] = datetime.datetime.fromtimestamp(float(post[2]))
```

9. Counting posts in March
--------------------------

```python
for post in posts: 
    if post[2].month == 3:
        march_count += 1
```

10. Counting posts in any month
-------------------------------

Making the above code snippet generic.

```python
def month_post_count(month):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = month_post_count(2)
aug_count = month_post_count(8)
```
