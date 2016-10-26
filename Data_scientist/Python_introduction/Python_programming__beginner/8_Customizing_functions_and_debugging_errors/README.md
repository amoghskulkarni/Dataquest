Data Scientist / Python Introduction / Python Programming: Beginner / Customizing functions and debugging errors
================================================================================================================

1. Overview
-----------

Overview of the last lesson

2. Multiple return paths
------------------------

One return in `if`, another in `else`. Kids stuff.

3. Optional arguments
---------------------

Actually about the default values that some arguments can take. For example, this code of
`tokenize()` function, which accepts an additional argument called `clean` depnding upon which the string will
be cleaned. If nothing is passed in place of `clean` argument, it won't be cleaned because the default value is
`False`. 

```python
def tokenize(text_string, special_characters, clean=False):
    # If `clean` is `True`.
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    # If `clean` not equal to `True`, no cleaning.
    story_tokens = text_string.split(" ")
    return(story_tokens)
```

4. Named arguments
------------------

You can pass the arguments so that they are not in the order as they have been specified in the function's signature.

```python
tokenized_story = tokenize(special_characters=clean_chars, text_string=story_string, clean=True)
```

5. Practice: Creating a more compact spell checker
--------------------------------------------------

`spell_check()` function is a wrapper around `clean_text()` and `tokenize()`, which opens `dictionary.txt` interanlly,
and uses updated version of `tokenize()`.

```python
def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()
    
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)
```

6. Python errors
----------------

- Two main types

Syntax and Runtime errors

7. Syntax errors
----------------

8. Runtime errors
-----------------

9. `TypeError` and `ValueError`
-------------------------------

`TypeError` will occur if mismatching of types is observed.

```python
forty_two = 42
forty_two + "42"
```

`ValueError` will occur when the type is correct but value is wrong.

```python
float('3.14')           # No errors
float('pi')             # ValueError
```

10. `IndexError` and `AttributeError`
-------------------------------------

`IndexError` are for invalid indices in case of lists and dictionaries, and `AttributeError` is for
invalid attributes of the objects.

11. Traceback
-------------

How to traceback the errors
