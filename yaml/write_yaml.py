# -*- coding: utf-8 -*-
''' Simple example writing a YAML file.'''
import yaml

days = [{'weekday' : ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']},
{'months' : ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']}]

with open('output.yaml', 'w') as file:
    outputs= yaml.dump(days, file)
file.close()
