import argparse
import sys
# from leap import isleap
from calendar import isleap
import re

parser = argparse.ArgumentParser(description= 'Pass in date in cmd line')
parser.add_argument('-d', '--date', metavar='', type=str, help= 'date in mm/dd/yyyy')
#add in mutually exclusive group for quiet vs verbose
group = parser.add_mutually_exclusive_group()
group.add_argument('-q,', '--quiet', action='store_true', help='print just result')
group.add_argument('-v,', '--verbose', action='store_true', help='print addl info (out anchor, doomsday, etc)')
args = parser.parse_args()

def user_input():
    date = input('Enter a date between 1/1/1800 and 12/31/2199:    ')
    return(date)

def date_parser(date):
    pattern = re.compile('(\d{1,2})\/(\d{1,2})\/(\d{2}(\d{2}))')
    string = date
    match=re.match(pattern,string)
    month = int(match.group(1))
    day = int(match.group(2))
    year = int(match.group(3))
    y = int(match.group(4))
    return(month, day, year, y)

def century(year):
    if year<=1899 and year>=1800:
        anchor = 5
    elif year<=1999 and year>=1900:
        anchor = 3
    elif year<=2099 and year>=2000:
        anchor = 2
    elif year<=2199 and year>=2100:
        anchor = 0
    else:
        print('Error: Year must be between 1800 and 2199')
    # if args.quiet:
    #     pass
    # else:
        # print('Anchor: ' + str(anchor))
    return(anchor)

        
def year_(y, anchor):
    doomsday= (( y//12 + y%12 + (y%12)//4 ) % 7  + anchor )%7
    # if args.quiet:
    #     pass
    # else:
        # print('Doomsday: ' +str(doomsday))
    return(doomsday)
   
#so far, we have a number that corresponds to the century and then the year. 

# 1/3, 2/28, 3/0, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12

# months = range(1,13)
# doomsdays = [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
# dooms_days = dict(zip(months, doomsdays))
# print(dooms_days)

def day_sub(month):
    l1= range(1,13)
    l2 = [4,0,0,3,5,1,3,6,2,4,0,2]
    d = dict(zip(l1,l2))
    n = d[month]
    # if args.quiet:
    #     pass
    # else:
    #     print('Month Contibution: '+ str(n))
    return(n)



def day_of_week(integer):
    days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    zipper= zip(range(7), days)
    codes= dict(zipper)
    return(codes[integer])

def main():
    if len(sys.argv) >1:     #means that user included the date in the cmd line 
        date = args.date  
    else:
        date = user_input()
    month, day, year, y = date_parser(date)
    anchor = int(century(int(year)))
    doomsday = int(year_(int(y), int(anchor)))
    n = day_sub(int(month))
    total = (doomsday +n + int(day))%7
    if isleap(year)==True:  #changed to include isleap module instead of just divisible by 4
        if month ==2 or 1:  #just changed to 1 from 3
            total = total-1
    day_ = day_of_week(total)
    if args.quiet:
        print(day_)
    elif args.verbose:
        print(date)
        print('Century Contribution = Anchor: ' + str(anchor))
        print('Year Contribution = Doomsday: ' +str(doomsday))
        print('Month Contibution: '+ str(n))
        print('Day of the Week for {} is: {}'.format(date,day_))


    else:
        print('Day of the Week for {} is: {}'.format(date,day_))

main()



# run date validation subroutine
# run month subroutine
# run day subroutine
# output answer
# want to add in an option for long format which gives you the doomsday for the given year
