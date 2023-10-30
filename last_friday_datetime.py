import datetime
from dateutil.relativedelta import FR, relativedelta

x= "08/2022"
def get_last_friday(d):
    d = datetime.datetime.strptime("01/" + d, "%d/%m/%Y")
    res = d + relativedelta(day=31, weekday=FR(-1))
    return print(res.strftime("%d.%m.%Y"))


get_last_friday(x)
