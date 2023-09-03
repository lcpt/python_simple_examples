# -*- coding: utf-8 -*-
''' Get the file name from the path.'''
import os

pth= '~/Documents/xc_projects/202309304359_proj/20_project_design/040_drawings/fitting_test.FCStd'

fileName= os.path.basename(pth)
print(fileName)
