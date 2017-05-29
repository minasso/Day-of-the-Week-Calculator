import argparse
import sys
parser = argparse.ArgumentParser(description= 'Add in date to day of week calculator')
parser.add_argument('-d', '--date', metavar='', type=str, help= 'date in mm/dd/yyyy')

if len(sys.argv) >1:
    date = sys.argv[1]
else:
    
