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

In Python, we use the `re` module to work with regular expressions.

Note that the second example in the table contains "habit" confirming to the Regex "..t".
Thus we know now that the only requirement is that the pattern given by the regex should be
a substring in the string that we are checking in.

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

5. Reading and printing the dataset
-----------------------------------

Nothing new. Use `csv.reader()` to print first 10 rows of the dataset.

```python
import csv
f = open("askreddit_2015.csv", "r")
posts_with_header = list(csv.reader(f))

posts = posts_with_header[1:]
for i, post in enumerate(posts):
    if i < 10:
        print(post)
```

6. Testing for matches
----------------------

`re` module is used for regex in Python. Using `re.search(regex, string)`, we can check if `string` is a match for `regex`. 
If it is, it will return a **match** object. If it isn't, it will return `None`.

Example - we can count a string in the posts using this

```python
import re

of_reddit_count = 0

for post in posts: 
    if re.search("of Reddit", post[0]) is not None:
        of_reddit_count += 1
```

7. Accounting for inconsistencies
---------------------------------

In Regex, `[]` are used to give the options that can be filled in a place.

Example - the regular expression `[bcr]at` would be matched by strings with the substrings `bat`, `cat`, and `rat`, but nothing else.

We can use `[]` for finding `of Reddit` and `of reddit` occurrances.

```python
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1
```

8. Escaping special characters
------------------------------

Use `\` (backslash) to escape special characters in Regex. 

Example - Suppose we wanted to match all strings that end with a period. If we used `.$`, it would match all strings that contain any 
character, since `.` has that special meaning. Instead, we must escape the `.` with a backslash, and our regular expression becomes `\.$`.

```python
for post in posts:
    if re.search("\[Serious\]", post[0]) is not None:
        serious_count += 1
```

9. Refining the search
----------------------

Modify the above code snippet to take into account `[Serious]` as well as `[serious]`.

```python
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1
```

10. Adding More Complexity to Your Regular Expression
-----------------------------------------------------

Modify the above code snippet to take into account `(Serious)` and `(serious)` tags as well.

```python
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1
```

11. Multiple regular expressions
--------------------------------

Now we'll write multiple regexes to match, and if either of them matches with the string, `re.search()` will return **match** object.

To combine regular expressions, we use the `|` character. For example, `cat|dog` would be matched by `catfish` and `hotdog`, since 
both these strings match either `cat` or `dog`.

```python
serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_start_count += 1

for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_end_count += 1

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_count_final += 1
```

12. Substituting strings
------------------------

Using `re.sub(pattern, repl, string)`, we can substitute a substring of `string` that is matched by regex given in `pattern` by 
a replacement string given by `repl`. `re.sub()` returns the original string if the pattern is not found, or the replaced string otherwise.

Example - Replace all kind of **serious** tags to `[Serious]`

```python
for post in posts:
    post[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", post[0])
    posts_new.append(post)
```

13. Matching years
------------------

- Ranges
`[a,b,c,d,e]` can be matched with any of the 5 characters specified. Same will be the result if the regex is `[a-e]`.

- Years
Years string are typically composed of 4 consecutive numbers. Regex `[0-9][0-9][0-9][0-9]` will do, but stronger checks can be made (like years
only after 999 and only before 3000 are matched).

```python
for string in strings:
    if re.search("[1,2][0-9][0-9][0-9]", string) is not None:
        year_strings.append(string)
``` 

14. Repeating regular expressions
---------------------------------

Repetating pattern can be specified by `{n}` syntax.

Example - If we were matching any 4-digit number, we could repeat the pattern `[0-9]` 4 times by writing `[0-9]{4}`, instead of 
writing `[0-9][0-9][0-9][0-9]`.

```python
for string in strings:
    if re.search("[1,2][0-9]{3}", string) is not None:
        year_strings.append(string)
```

15. Extracting years
--------------------

`re.findall(regex, string)` returns a list of substrings that match the provided `regex`. 

Example - `re.findall("[a-z]", "abc123")` would return `["a", "b", "c"]`, since those are the substrings that match the regex.

```python
years = re.findall("[1,2][0-9]{3}", years_string)
```
