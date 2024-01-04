import pandas as pd
import matplotlib.pyplot as plt

df_shootings = pd.read_csv('fatal-police-shootings-data.csv')

pivot_table = pd.pivot_table(df_shootings, values='id', index=['race'], columns=['signs_of_mental_illness'],
                             aggfunc='count')
print(pivot_table)

pivot_table['percentage_of_mental_illness_per_race'] = pivot_table.apply(
    lambda row: row[True] * 100 / (row[True] + row[False]), axis=1)
print(pivot_table)
print(pivot_table['percentage_of_mental_illness_per_race'].idxmax())
df_shootings['weekday'] = pd.to_datetime(df_shootings['date']).dt.weekday
by_weekdays = df_shootings['weekday'].value_counts().sort_index()
fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(by_weekdays.index, by_weekdays.values, color='indianred')
ax.set_xticks(by_weekdays.index)
ax.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
ax.set_title('Amount of shootings by weekdays')
plt.show()

data_states_by_population = pd.read_html(
    'https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population',
    header=0)
df_states = pd.DataFrame(data_states_by_population[0])
difference = df_states.columns.difference(
    ['Rank in states & territories, 2020', 'State', 'Percent of the total U.S. population, 2020 [note 3]'])
df_states = df_states.drop(difference, axis=1)
print(df_states)

data_state_territory_abbreviations = pd.read_html(
    'https://www.ssa.gov/international/coc-docs/states.html')
df_abbr = data_state_territory_abbreviations[0]
df_abbr['0'] = df_abbr['0'].apply(str.lower)
print(df_abbr)
