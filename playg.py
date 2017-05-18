import re


def user_input():
    date = input('Enter a date between 1/1/1800 and 12/31/2199')
    print(date)
    return(date)

def date_parser(date):
    pattern = re.compile('(\d{1,2})\/(\d{1,2})\/(\d{2}(\d{2}))')
    string = date
    match=re.match(pattern,string)
    month = match.group(1)
    day = match.group(2)
    year = match.group(3)
    y = match.group(4)
    print(month, day, year, y)
    return(month, day, year, y)
    # return({'month': month, 'day': day, 'year': year, 'y': y})

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
    return(anchor)

def year_(y, anchor):
    doomsday= (( y//12 + y%12 + (y%12)//4 ) % 7  + anchor )%7
    return(doomsday)


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
    return(n)


def day_of_week(integer):
    days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    zipper= zip(range(7), days)
    codes= dict(zipper)
    return(codes[integer])

def main(date):
    month, day, year, y = date_parser(date)
    anchor = int(century(int(year)))
    doomsday = int(year_(int(y), int(anchor)))
    n = day_sub(int(month))
    total = (doomsday +n + int(day))%7
    if int(y)%4==0:
        if month ==2 or 3:
            total = total-1
    day_ = day_of_week(total)
    print(day_)

d='12/31/1986'
d1='3/13/2017'
d2='4/1/2017'
d3='2/29/2016'
d4='11/30/1983'
main(d)










# run date validation subroutine
# run month subroutine
# run day subroutine
# output answer
