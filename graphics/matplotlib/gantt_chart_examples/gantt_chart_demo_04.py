"""
GANTT Chart with Matplotlib

Based on the code in:
https://www.datacamp.com/tutorial/how-to-make-gantt-chart-in-python-matplotlib
"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

df = pd.DataFrame({'task': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
                  'team': ['R&D', 'Accounting', 'Sales', 'Sales', 'IT', 'R&D', 'IT', 'Sales', 'Accounting', 'Accounting', 'Sales', 'IT'],
                  'start': pd.to_datetime(['20 Oct 2022', '24 Oct 2022', '26 Oct 2022', '31 Oct 2022', '3 Nov 2022', '7 Nov 2022', '10 Nov 2022', '14 Nov 2022', '18 Nov 2022', '23 Nov 2022', '28 Nov 2022', '30 Nov 2022']),
                  'end': pd.to_datetime(['31 Oct 2022', '28 Oct 2022', '31 Oct 2022', '8 Nov 2022', '9 Nov 2022', '18 Nov 2022', '17 Nov 2022', '22 Nov 2022', '23 Nov 2022', '1 Dec 2022', '5 Dec 2022', '5 Dec 2022']),
                  'completion_frac': [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0]})

# 1 How many days passed/would pass from the overall project start to the
# start date of each task:
df['days_to_start'] = (df['start'] - df['start'].min()).dt.days

# 2 How many days passed/would pass from the overall project start to the
# end date of each task:
df['days_to_end'] = (df['end'] - df['start'].min()).dt.days

# 3 The duration of each task, including both the start and end dates:
df['task_duration'] = df['days_to_end'] - df['days_to_start'] + 1  # to include also the end date

# 4 The status of completion of each task translated from a fraction into a
# portion of days allocated to that task:
df['completion_days'] = df['completion_frac'] * df['task_duration']

print(df)

# 1
team_colors = {'R&D': 'c', 'Accounting': 'm', 'Sales': 'y', 'IT': 'b'}
patches = []
for team in team_colors:
    patches.append(matplotlib.patches.Patch(color=team_colors[team]))

# 2
fig, ax = plt.subplots()

# 3
xticks = np.arange(5, df['days_to_end'].max() + 2, 7)
for index, row in df.iterrows():
    # plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']])
    
    # Adding a lower bar - for the overall task duration
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']], alpha=0.4)

    # Adding an upper bar - for the status of completion
    plt.barh(y=row['task'], width=row['completion_days'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

# 4
xticklabels = pd.date_range(start=df['start'].min() + dt.timedelta(days=4), end=df['end'].max()).strftime("%d/%m")
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])
ax.xaxis.grid(True, alpha=0.5)

# Adding a legend
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)

# Marking the current date on the chart
ax.axvline(x=29, color='r', linestyle='dashed')
ax.text(x=29.5, y=11.5, s='17/11', color='r')

plt.show()
