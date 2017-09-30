Data Scientist / Python Introduction / Python Programming: Beginner / Debugging
===============================================================================

1. Types of Errors
------------------

- Syntax errors
- Runtime errors

2. Syntax errors
----------------

3. Runtime errors
-----------------

4. TypeError and ValueError
---------------------------

- `TypeError`
```python
forty_two = 42
forty_two + "42"
```

- `ValueError`
```python
float("guardians")
```

5. IndexError and AttributeError
--------------------------------

- `IndexError`
```python
lives = [1,2,3]
lives[4]
```

- `AttributeError`
```python
f = open("story.txt")
f.split(" ")
```
This occurs when we try to call a method or attribute on an object that doesn't contain it. 
In the above code snippet, we try to call the `split()` method on the File handler instance, 
instead of using the `read()` method to read it into a string first.

`TextIOWrapper` is a built-in Python object that represents the File handler. It does not 
contain the `split()` method. Since the Python interpreter couldn't find the `split()` method 
within the `TextIOWrapper` class, it returned an instance of `AttributeError`.

6. Traceback
------------

The traceback shows the series of function calls that occurred. The topmost function call 
is the highest level of code we wrote, and oftentimes the section we need to fix. The last 
function call is where the error actually occurred.


