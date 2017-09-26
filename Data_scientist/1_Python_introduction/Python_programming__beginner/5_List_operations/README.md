Data Scientist / Python Introduction / Python Programming: Beginner / List Operations
=====================================================================================

1. The dataset
--------------

```python
Day,Type of Weather
1,Sunny
2,Sunny
3,Sunny
4,Sunny
5,Sunny
6,Rain
7,Sunny
8,Sunny
9,Fog
10,Rain
...
```

`Day` - A number from `1` to `365`

`Type of Weather` - Type of weather. Can be one of `Rain`, `Sunny`, `Fog`, `Fog-Rain` or `Thunderstorm`

2. Parsing the file
-------------------

```python
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split("\n")
weather_data = []
for row in rows:
    weather_data.append(row.split(','))
```

`weather_data` looks something like -

```python
[['Day', 'Type of Weather'], ['1', 'Sunny'], ['2', 'Sunny'], ...]
```

3. Getting a single column from the data
----------------------------------------

- Stupid approach

```python
weather = []

for wd in weather_data:
    weather.append(wd[1])
```

- There is a better approach to this. More on that in the next lessons.

4. Counting the items in a list
-------------------------------

Are you kidding me? 

- Stupid approach

```python
count = 0
for item in weather:
    count = count + 1
```

5. Slicing lists
----------------

```python
slice_me = [7, 6, 4, 5, 6]
slice_me[0:3]           # [7, 6, 4]
slice_me[1:2]           # [6]
slice_me[2:2]           # []
```

6. Practice: Slicing lists
--------------------------

7. Removing the header
----------------------

- Header

(Usually) the first line of the dataset explaining what the column contains

- Slicing the 1st element

```python
weather_no_header = weather[1:]
```

8. The `in` statement
---------------------

- Tells if a certain element is present _in_ the list

- Example

```python
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    if animal == "cat":
        print("Cat found")
```

is equivalent to

```python
animals = ["cat", "dog", "rabbit"]
if "cat" in animals:
    print("Cat found")
```

9. Weather types
----------------

We can use the in statement to discover which types of weather the new_weather list contains.

```python
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for weather_type in weather_types:
    weather_type_found.append(weather_type in new_weather)
```
