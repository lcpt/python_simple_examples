# -*- coding: utf-8 -*-
''' Remove the file name from the path.'''
import os

fileName= '~/Documents/xc_projects/202309304359_proj/20_project_design/040_drawings/fitting_test.FCStd'

pth= os.path.dirname(fileName)
print(pth)
