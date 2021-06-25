from datetime import datetime

#Year
def get_year(x):
    dateStr=x.split()[0]
    dateDT=datetime.strptime(dateStr,"%Y-%m-%d")
    year=dateDT.year
    return year

#Month
def get_month(x):
    dateStr=x.split()[0]
    dateDT=datetime.strptime(dateStr,"%Y-%m-%d")
    month=dateDT.month
    return month

#Week
def get_weekday(x):
    dateStr=x.split()[0]
    dateDT=datetime.strptime(dateStr,"%Y-%m-%d")
    week_day=dateDT.weekday()
    return week_day

#Day
def get_date(x):
    dateStr=x.split()[0]
    dateDT=datetime.strptime(dateStr,"%Y-%m-%d")
    return dateDT

#Hour
def get_hour(x):
    hour=x.split()[1].split(":")[0]
    int_hour=int(hour)
    return int_hour