import argparse
import sys
from calendar import isleap
import re

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Pass in date in cmd line')
    parser.add_argument('-d', '--date', metavar='', type=str, help= 'date in mm/dd/yyyy')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q,', '--quiet', action='store_true', help='print just result')
    group.add_argument('-v,', '--verbose', action='store_true', help='print addl info (out anchor, doomsday, etc)')
    args = parser.parse_args()
    return(args)

def user_input():
    date = input('Enter a date between 1/1/1800 and 12/31/2199 in MM/DD/YYYY form:    ')
    return(date)

#can get rid of re if i just split at /

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
    return(anchor)

def year_(y, anchor):
    doomsday= (( y//12 + y%12 + (y%12)//4 ) % 7  + anchor )%7
    return(doomsday)
   
def day_sub(month):
    l1= range(1,13)
    l2 = [4,0,0,3,5,1,3,6,2,4,0,2]    
    d = dict(zip(l1,l2))
    n = d[month]
    return(n)

def day_of_week(integer):
    days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    zipper= zip(range(7), days)
    codes= dict(zipper)
    return(codes[integer])

def data_validation(month, day, year):
    if month not in range(1,13):
        print('Month must be between 01 and 12')
        return(False)
    elif day not in range(1,32):
        print('Day must between 01 and 31')
        return(False)
    elif year not in range(1800,2200):
        print('Year must be between 1800 and 2199')
        return(False)
    else:
        return(True)
    
def main():
    data_valid=False
    i=0
    while (data_valid==False) and (i<3):
        i+=1
        if i>5:
            exit()
        if len(sys.argv) >1:   
            args = argument_parser()  
            date = args.date  
        else:
            date = user_input()
        month, day, year, y = date_parser(date)
        print(month, day, year, y)
        data_valid=data_validation(month, day, year)


    anchor = int(century(int(year)))
    doomsday = int(year_(int(y), int(anchor)))
    n = day_sub(int(month))
    total = (doomsday +n + int(day))%7
    if isleap(year)==True:  
        if month ==2 or 1:  
            total = total-1
    day_ = day_of_week(total)

    if len(sys.argv) >1:
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

if __name__ == '__main__':
    main()



