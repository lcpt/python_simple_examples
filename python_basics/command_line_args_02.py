from __future__ import print_function
import sys
import logging
from pathlib import Path

if(len(sys.argv)<2):
    logging.error('Syntax: '+sys.argv[0]+ ' input_file_name')
    quit()


inputFileName= sys.argv[1]
outputFileName= Path(inputFileName).stem+'.yaml'

print('inputFileName: ', inputFileName)
print('outputFileName: ', outputFileName)
