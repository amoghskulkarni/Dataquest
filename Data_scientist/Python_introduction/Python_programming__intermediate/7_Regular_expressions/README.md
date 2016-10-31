Data Scientist / Python Introduction / Python Programming: Intermediate / Regular expressions
=============================================================================================

1. Regular expressions
----------------------

A regular expression is a sequence of characters that describes a search pattern. 

In practice, we say that certain strings match a regular expression if the pattern can be found
anywhere within those strings (as a substring). The simplest example of regular expressions is 
an ordinary sequence of characters. Any string that contains that sequence of characters, all 
adjacent and in the proper order, is said to match that regular expression. 

Example -

Regex | Example matches | Example that don't match
:---:|:---:|:---:
123 | 12345, abc123def, 123 | 1a2b3c, 321
b | b, abc, bread | xyz, c, B

```python
strings = ["data science", "big data", "metadata"]
regex = "data"
```

2. Special characters
---------------------

The special character `.` is used to indicate that any character can be put in its place. 
Here are a few examples:

Regex | Example matches | Example that don't match
:---:|:---:|:---:
a.c | aac, abc, acc, alchemy, branch | add, crash
..t | bat, habit, oat | at, it

In Python, we use the re module to work with regular expressions.

```python
strings = ["bat", "robotics", "megabyte"]
regex = "b.t"
```

3. Beginnings and ends of strings
---------------------------------

We can use `^` to match the start of a string and `$` to match the end of string.

Example -

`^a` will match all strings that start with `a`.  
`a$` will match all strings that end with `a`.

```python
strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"
```

4. Dataset: AskReddit data
--------------------------

1000 datapoints of top 1000 Reddit posts of 2015, each row datapoint containing -

Field | Description
:---: | :----:
Title | The title of the post
Score | The number of upvotes the post received
Time | When the post was posted
Gold | How much Reddit Gold was given to the post
NumComs | Number of comments the post received
