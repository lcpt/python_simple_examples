# -*- coding: utf-8 -*-
''' Compute root mean sqare error.'''
import math
import numpy as np

y_actual = [1,2,3,4,5]
y_predicted = [1.6,2.5,2.9,3,4.1]
 
MSE= np.square(np.subtract(y_actual,y_predicted)).mean() 
 
RMSE= math.sqrt(MSE)
print("Root Mean Square Error:", RMSE)
