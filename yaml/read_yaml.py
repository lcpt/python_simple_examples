# -*- coding: utf-8 -*-
''' Simple example writing a YAML file.'''
import yaml

with open('output.yaml') as file:
    try:
        data= yaml.safe_load(file)
        lstA= data[0]
        #print(lstA)
        print('days of the week: ',lstA['weekday'])
        lstB= data[1]
        #print(lstB)
        print('months of the year: ',lstB['months'])
    except yaml.YAMLError as exception:
        print(exception)
