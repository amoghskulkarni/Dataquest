Data Scientist / Python Introduction / Python Programming: Intermediate / Variable scopes
=========================================================================================

1. The dataset
--------------

A dataset that contains information on student loan defaults in the United States.
Some of the columns are -

Column | Description
:------|:----------
`institution` | the name of the university.
`state` | the state the university is in.
`city` | the city the university is in.
`borrower_default_count_240` | the total number of students who have defaulted on their loans.
`principal_outstanding_240` | the total amount of the loans in default.

2. Built-in functions
---------------------

- `sum()`
- `len()`
- `float()`
- `min()`
- `max()`

3. Overwriting a built-in function
----------------------------------

The example given is more like 'Overriding' the `sum()`.

```python
b = [1,2]
sum = sum(b)
sum([3, 4, 5, 6]])         # Causes error, because definition of sum() has been overridden
```

4. Scopes
---------

Local and global scopes of the variables in context of functions.

5. Scope isolation
------------------

Local scopes are not only separate from the global ones, but two local scopes are isolated from
each other as well. 

E.g. two functions defined in the global scope 

6. Scope inheritance
--------------------

When a variable name is used in a _local_ scope, but it hasn't been defined in the scope yet, 
the Python interpreter will check to see if the variable exists in the _global_ scope.

In the following code snippet, `principal_outstanding_240` is a variable that holds all the entries
from the currosponding column from data `student_loan_defaults.csv`. 

```python
def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10
average = find_average(principal_outstanding_240)
```

7. Inheritance limits
---------------------

We can access the value of a global scope variable inside a local scope, but we can't change 
the value of that variable. The code below will cause an error -

```python
a = 2
def alter_a():
    a = a * 2
    return a
```

In other words, the variables inherited from the global scope are _write protected_. 

8. Built-in inheritance
-----------------------

If a variable is used in a _local_ scope, but it isn't defined, the Python interpreter will first 
look in the _global_ scope. If it doesn't find the variable there, it will then look to see if the 
variable is a _built-in_ function name.

The code below will cause an error, becauase `sum()` will not be looked into _built-in_ scope once
the interpreter finds it in the _global_ scope -

```python
sum = 10

def total(a):
    return sum(a)

print(total([1,2]))
```

9. Global variables
-------------------

We can make _global_ variables updatable in local scopes using `global` keyword, as -

```python
global total
total = 10

def add_to_total(a):
    total = total + a

add_to_total(20)
print(total)
```

The above code will print `30` as the function will access the global variable.

**The _global_ variables can be declared inside a local scope as well**. 

```python
def test_function():
    global a
    a = 10

test_function()
print(a)
```

The above code will print `10`.

10. Inheritance rules
---------------------

When you use a variable anywhere in a Python script, the Python interpreter will look 
for the value of that variable using some simple rules:

- First start with the _local_ scope, if any. If the variable is defined here, use the value.
- Look at any _enclosing_ scopes, starting with the innermost. These are "outside" local scopes. 
If the variable is defined in any of them, use the value.
- Look in the _global_ scope. If the variable is there, use the value.
- Finally, look in the _built-in_ functions.
- If no value is found, an error will be thrown.

A simple way to remember this is **LEGBE**, which stands for "Local, Enclosing, Global, Built-ins, Error".

