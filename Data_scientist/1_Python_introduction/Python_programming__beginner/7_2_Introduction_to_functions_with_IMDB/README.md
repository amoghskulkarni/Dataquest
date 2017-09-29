Data Scientist / Python Introduction / Python Programming: Beginner / Introduction to functions
===============================================================================================

1. Overview
-----------

Goal is to create a function to parse a csv file and return its elements. `movie_metadata.csv` is a CSV file containing 
the dataset of IMDB containing the data in the following format -

2. Motivating Functions
-----------------------

"a function is a packaged body of code that we can reuse by calling with the relevant parameters";
3 main advantages of using functions, **information hiding**, **modularity**, **abstraction**;
blah, blah

3. Writing Our Own Functions
----------------------------

Write a function, with a definition, name, argument(s), body and return value, that returns a list containing the names 
of the movies in `movie_data`. This function is expected to behave similar to `first_elt()`, but for multiple lists.

```python
def first_elts(input_lst):
    elts = []
    for each in input_lst:
        elts.append(each[0])
    return elts

movie_names = first_elts(movie_data)
print(movie_names[0:5])
```

4. Functions with Multiple Return Paths
---------------------------------------

Write a function named is_usa() that checks whether or not a movie was made in the United States.

```python
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
```

5. Functions with Multiple Arguments
------------------------------------

Make the above function generic, for that, 
write a function index_equals_str() that takes in three arguments: a list, an index and a string, and checks whether that 
index of the list is equal to that string.

```python
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
```

6. Optional Arguments
---------------------

Write a function, combining `index_equals_str()` and `counter()`, which counts the number of elements that fulfill the requirement
`index_equals_str()`.

```python
# Given functions
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt
```

Answer is -

```python
def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
```

`header_row` is an optional argument here (which is by default `False`), which shows whether the data being passed has the 
header row in it.
