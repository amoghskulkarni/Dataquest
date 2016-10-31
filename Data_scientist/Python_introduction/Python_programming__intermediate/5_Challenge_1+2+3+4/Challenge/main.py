### Read this dataset into Python and explore the data to become more familiar with it.

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

### Explore the values in these columns by using sets and list comprehensions.

# Use list comprehensions and the set function to create a set of the unique values in the team column.
# Assign this set to unique_teams.
teams_col = 1
teams_list = [susp[teams_col] for susp in nfl_suspensions]
unique_teams = set(teams_list)

# Use list comprehensions and the set function to create a set of the unique values in the games column.
# Assign this set to unique_games.
games_col = 2
games_list = [susp[games_col] for susp in nfl_suspensions]
unique_games = set(games_list)

### Create a Suspension class that we can use to represent each NFL suspension in the dataset.
class Suspension():
    # Class representing a row in a dataset
    def __init__(self, s):
        name_col = 0
        self.name = s[name_col]
        self.teams = s[teams_col]
        self.games = s[games_col]
        # self.year = s[year_col]
        ### Instead of assigning the value at index 5 to the year property directly, use a try except block
        try:
            self.year = int(s[year_col])
        except:
            self.year = 0

    def get_year(self):
        return self.year



