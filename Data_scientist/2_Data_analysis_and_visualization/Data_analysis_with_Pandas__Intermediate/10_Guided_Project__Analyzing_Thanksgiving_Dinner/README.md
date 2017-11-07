# Data Scientist / Data Analysis and Visualization / Data Analysis with Pandas: Intermediate / Guided Project: Analyzing Thanksgiving Dinner

## Introducing Thanksgiving Dinner Data

-----

The dataset is stored in the `thanksgiving.csv` file. It contains `1058` responses to an online survey about what Americans eat for Thanksgiving dinner. Each survey respondent was asked questions about what they typically eat for Thanksgiving, along with some demographic questions, like their gender, income, and location. 

The dataset has `65` columns, and `1058` rows. Most of the column names are questions, and most of the column values are string responses to the questions. Most of the columns are categorical (i.e. Enum), as a survey respondent had to select one of a few options.

There are also quite a few `NaN` values in the columns, which occurred when a survey respondent didn't fill out a question because they didn't want to, or it didn't apply to them.

## Filtering Out Rows From A DataFrame

-----

Because we want to understand what people ate for Thanksgiving, we'll remove any responses from people who don't celebrate it. The column `Do you celebrate Thanksgiving?` contains this information. We only want to keep data for people who answered `Yes` to this questions.

ere we use [`pandas.Series.value_counts()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) to get what values are present in the column and then use them to filter out the rows containing `Yes`. 

## Using value_counts To Explore Main Dishes

-----

Let's explore what main dishes people tend to eat during Thanksgiving dinner. We can again use the `value_counts` method to help us with this.

## Figuring Out What Pies People Eat

-----

We'll look at how many people eat `Apple`, `Pecan`, or `Pumpkin` pie during Thanksgiving dinner. This data is encoded in the following three columns:

- `Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple`
- `Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin`
- `Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan`

In all three columns, the value is either the name of the pie if the person eats it for Thanksgiving dinner, or null otherwise. We can find out how many people eat one of these three pies for Thanksgiving dinner by figuring out for how many people all three columns are null. Use `pandas.isnull()` which returns boolean series. We can use this to find out the people who ate at least one kind of pie.

## Converting Age To Numeric

-----

Use `pandas.Series.apply()` to operate the age column which has string values and convert it into numeric column. `pandas.series.describe()` can be used to gain useful statistics after ensuring all the entries in a column are numeric.

## Converting Income To Numeric

-----

The `How much total combined money did all members of your HOUSEHOLD earn last year?` column is very similar to the `Age` column. Has string values, but in terms of categories which can be converted to numercical values. 

## Correlating Travel Distance And Income

-----

We can now see how the distance someone travels for Thanksgiving dinner relates to their income level. It's safe to hypothesize that people earning less money could be younger, and would travel to their parent's houses for Thanksgiving. We can test this by filtering `data` based on `int_income`, and seeing what the values in the `How far will you travel for Thanksgiving?` column are.

## Linking Friendship And Age

There are two columns which directly pertain to friendship, `Have you ever tried to meet up with hometown friends on Thanksgiving night?`, and `Have you ever attended a "Friendsgiving"?`. In the US, a "Friendsgiving" is when instead of traveling home for the holiday, you celebrate it with friends who live in your area. Both questions seem skewed towards younger people. Let's see if this hypothesis holds up.

We use `pandas.DataFrame.pivot_table()` for this.


