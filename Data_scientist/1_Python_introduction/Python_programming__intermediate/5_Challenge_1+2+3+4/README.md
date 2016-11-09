Data Scientist / Python Introduction / Python Programming: Intermediate / Challenge: Modules, Classes, Error Handling, and List Comprehensions
==============================================================================================================================================

Dataset we are working on is `nfl_suspensions_data.csv`, which looks like -

Header | Definition
-------|-----------
`name` | first initial.last name
`team` | team at time of suspension
`games` | number of games suspended (one regular season = 16 games)
`category` | personal conduct, substance abuse, peformance enhancing drugs or in-game violence
`desc.` | description
`year` | year of suspension
`source` | news source

This challenge contains everything learnt in lessons 1, 2, 3 and 4 and Dataquest strongly encourages creating a project on personal computer
to complete this challenge. So entire challenge is completed in PyCharm on my personal computer and source code is kept in the repo.

Steps:

- Read this dataset into Python and explore the data to become more familiar with it
- Explore the values in these columns by using sets and list comprehensions
    - `unique_teams`
    - `unique_games`
- Create a `Suspension` class that we can use to represent each NFL suspension in the dataset
    - Has `name`, `teams`, `games` and `year` as its datamembers
- Tweak the `Suspension` class to add more features 
    - Instead of assigning the value at index 5 to the year property directly, use a try except block
    - Implement `get_year()` method which returns year

