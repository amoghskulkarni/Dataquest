Data Scientist / Python Introduction / Python Programming: Intermediate / Challenge: Modules, Classes, Error Handling, and List Comprehensions
==============================================================================================================================================

The raw data behind the story, [The NFL’s Uneven History Of Punishing Domestic Violence](http://fivethirtyeight.com/features/nfl-domestic-violence-policy-suspensions/).
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
```python
# Read the dataset into a list of lists.
import csv
nfl_file = open("nfl_suspensions_data.csv", "rU")
nfl_suspensions = list(csv.reader(nfl_file))

# Remove the first list in nfl_suspensions since it's the header row
nfl_suspensions = nfl_suspensions[1:]

# Count up the frequency for each value in the year column.
years = {}
year_col = 5
for susp in nfl_suspensions:
    row_year = susp[year_col]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1
```

- Explore the values in these columns by using sets and list comprehensions
    - `unique_teams`
    - `unique_games`
```python
team_col = 1
game_col = 2

teams = [row[team_col] for row in nfl_suspensions]
unique_teams = set(teams)
print(unique_teams)

games = [row[game_col] for row in nfl_suspensions]
unique_games = set(games)
print(unique_games)
```

- Create a `Suspension` class that we can use to represent each NFL suspension in the dataset
    - Has `name`, `teams`, `games` and `year` as its datamembers
```python
### Create a Suspension class that we can use to represent each NFL suspension in the dataset.
class Suspension():
    # Class representing a row in a dataset
    def __init__(self, s):
        name_col = 0
        teams_col = 1
        games_col = 2
        year_col = 5
        self.name = s[name_col]
        self.teams = s[teams_col]
        self.games = s[games_col]
        self.year = s[year_col]
```

- Tweak the `Suspension` class to add more features 
    - Instead of assigning the value at index 5 to the year property directly, use a try except block
    - Implement `get_year()` method which returns year
```python
class Suspension():
    def __init__(self,row):
        name_col = 0
        teams_col = 1
        games_col = 2
        year_col = 5

        self.name = row[name_col]
        self.team = row[teams_col]
        self.games = row[games_col] 
        ### Instead of assigning the value at index 5 to the year property directly, use a try except block
        try:
            self.year = int(row[year_col])
        except Exception:
             self.year = 0

    def get_year(self):
        return(self.year)
                
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
```

