# -*- coding: utf-8 -*-
''' Gantt chart test.

Code obtained from: https://plotly.com/python/gantt/''' 

import os
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
# fig.show()

fname= os.path.basename(__file__)
output_file_name= os.path.splitext(fname)[0]+'.png'
fig.write_image(output_file_name)
