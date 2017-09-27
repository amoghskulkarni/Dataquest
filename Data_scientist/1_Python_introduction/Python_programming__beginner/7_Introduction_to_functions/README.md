Data Scientist / Python Introduction / Python Programming: Beginner / Introduction to functions
===============================================================================================

1. Overview
-----------

Goal is to build a spell-checker. The file `dictionary.txt` is a plain text file containing a sequence of 
correctly spelled words. `dictionary.txt` consists of 1 line of text, where each word in that line is 
separated by a single whitespace `(" ")`.

2. Tokenizing the vocabulary
----------------------------

- Tokenization

Converting text into a set of individual components

The goal of tokenization is to convert a large body of text into smaller tokens, or components, that we can work with. 
In this case, each token is a word in the vocabulary.

- Use `split(' ')` to break the large string into multiple words

3. Replacing special characters
-------------------------------

Some words contain punctuations like `,` or `;`. Replace them using `replace()` method of the `string` class.

Example -

```python
text = "Howdy,my,name"
text = text.replace(",", "")
print(text)             # Howdymyname
``` 

4. Functions
------------

Some rant about what functions are and how they are used in software.

5. Practice: Creating a function to clean text
----------------------------------------------

- Syntax

Function name, arguments, function body, return value

```python
def clean_text(string_value):
    cleaned_value = string_value.replace(",", "")
    return(cleaned_value)
```

6. Lowercasing the words
------------------------

`lower()` method of the `string` will do the job.

Example -

```python
words = "Michael JACKSON Thriller"
lower_words = words.lower()
print(lower_words)          # michael jackson thriller
```

7. Multiple arguments
---------------------

Blah, blah, multiple arguments, blah, blah.

```python
def clean_text(text_string, strip_string):
    cleaned_string = ""
    replacement_string = ""
    cleaned_string = text_string.replace(strip_string, replacement_string)
    return(cleaned_string)
```

8. Tokenizing the story
-----------------------

Write `tokenize()` function which tokenizes the string passed in the argument. It also cleans the string.

Change `clean_text()` to accept a list of strings as the second argument instead of a single character.

```python
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)
```

9. Finding misspelled words
---------------------------

Check each token in the `tokenized_story` for being in `tokenized_vocabulary`. Quite straightforward.

```python
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
```
