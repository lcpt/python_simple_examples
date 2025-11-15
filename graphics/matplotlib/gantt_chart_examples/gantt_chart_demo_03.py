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

# Now, we're ready to generate a basic Gantt chart in matplotlib:

plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.show()

# When some tasks contain two or more subtasks spread out over a period of time, we should use another matplotlib method – broken_barh().

# To have some dummy data to try this approach on, let's do the following:

#  1   Take from our initial dataframe only those tasks assigned to the
#      Sales team (for now, let's ignore the completion_frac column).

df2 = df[df['team']=='Sales'][['task', 'team', 'start', 'end']]

#  2   Rename the columns start and end to start_1 and end_1 correspondingly
#      (for convenience).

df2.rename(columns={'start': 'start_1', 'end': 'end_1'}, inplace=True)
df2.reset_index(drop=True, inplace=True)

#  3   Add more subtasks to some of the available tasks.

df2['start_2'] = pd.to_datetime([None, '10 Nov 2022', '25 Nov 2022', None])
df2['end_2'] = pd.to_datetime([None, '14 Nov 2022', '28 Nov 2022', None])
df2['start_3'] = pd.to_datetime([None, None, '1 Dec 2022', None])
df2['end_3'] = pd.to_datetime([None, None, '5 Dec 2022', None])

#  4   For each subtask, calculate the three columns as shown above
#      representing the following information:
#         - How many days passed/would pass from the overall project start to
#           the start date of each subtask.
#         - How many days passed/would pass from the overall project start to
#           the end date of each subtask.
#         - The duration of each subtask, including both the start and end
#           dates.
for i in [1, 2, 3]:
    suffix = '_' + str(i)
    df2['days_to_start' + suffix] = (df2['start' + suffix] - df2['start_1'].min()).dt.days
    df2['days_to_end' + suffix] = (df2['end' + suffix] - df2['start_1'].min()).dt.days
    df2['task_duration' + suffix] = df2['days_to_end' + suffix] - df2['days_to_start' + suffix] + 1


print(df2)

# Note that now task D has two subtasks, task H has three subtasks, and tasks
# C and K have one subtask each. Hence, tasks D and H are those tasks for
# which we're going to apply the broken_barh() method. Since the syntax of
# this method is a bit less intuitive than that of barh(), let's take a look
# at its main parameters and their format. The mandatory parameters of the
# broken_barh() method are:

#     xranges – a sequence of tuples of the format (xmin, xwidth) to denote
#               the start and extension of each bar. Here, each bar represents
#               a subtask. So, this parameter displays the start date and
#               duration of each subtask.
#     yrange – a tuple of the format (ymin, yheight) to denote the y-position
#              and height for each bar.

# Now, let's plot our "broken" Gantt chart. The algorithm is as follows:

#     Create a figure with subplots.
#     Iterate through the rows of the dataframe and check if the task has
#     one, two, or three subtasks. Based on that, do the following:
#         - One subtask: plot a bar using the barh() method as we did earlier.
#         - Two subtasks: plot two bars using the broken_barh() method.
#         - Three subtasks: plot three bars using the broken_barh() method.
#     Add basic adjustments: set and label ticks of the y-axis.

# 1
fig, ax = plt.subplots()

# 2
for index, row in df2.iterrows():
    if row['start_2'] is None:
        # ax.barh(y=df2['task'], width=df2['task_duration_1'], left=df2['days_to_start_1'])
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1'])], yrange=(index + 1, 0.5))
    elif row['start_2'] is not None and row['start_3'] is None:
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1']), (row['days_to_start_2'], row['task_duration_2'])], yrange=(index + 1, 0.5))
    else:
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1']), (row['days_to_start_2'], row['task_duration_2']), (row['days_to_start_3'], row['task_duration_3'])], yrange=(index + 1, 0.5))

# 3
ax.set_yticks([1.25, 2.25, 3.25, 4.25])
ax.set_yticklabels(df2['task'])

plt.show()
