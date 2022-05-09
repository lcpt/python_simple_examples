from __future__ import print_function
import sys
import logging
from pathlib import Path

if(len(sys.argv)<2):
    logging.error('Syntax: '+sys.argv[0]+ ' input_file_name')
    quit()


inputFile= sys.argv[1]
outputFile= Path(inputFile).stem+'.yaml'

print('inputFile: ', inputFile)
print('outputFile: ', outputFile)
