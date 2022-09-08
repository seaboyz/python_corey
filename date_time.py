import datetime
from locale import D_T_FMT
from time import strptime
import pytz

# d = datetime.date(2022,9,8)
# print(d)

# tday = datetime.date.today()
# print(tday)
# print(tday.weekday())
# print(tday.isoweekday())

""" tdelta = datetime.timedelta(days=7)
print(tdelta)
# one week before
print(datetime.date.today() + datetime.timedelta(days=7))
# one week after
print(datetime.date.today() - datetime.timedelta(days=7)) """

""" # Bithday from today
print(datetime.date(2022,12,22)-datetime.date.today())
print((datetime.date(2022,12,22)-datetime.date.today()).days)
print((datetime.date(2022,12,22)-datetime.date.today()).total_seconds())
 """

""" t = datetime.time(9,30,45,100000)
print(t.hour) """

""" dt = datetime.datetime(2022,9,8,8,43,1)
print(dt)
print(dt.time())
print(dt.date())

tdeltal = datetime.timedelta(days=7)

print(dt + tdeltal) """

""" # current local time
dt_today = datetime.datetime.today()
# option open to timezone
dt_now = datetime.datetime.now()
# utc time zone
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow) """

""" 
# timezone aware
dt = datetime.datetime(2022, 9, 8, 9, 8, 1, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utc_now)
print(dt_utc_now.astimezone(pytz.timezone('US/Mountain')))
for tz in pytz.all_timezones:
    print(tz)
print(dt_utc_now.astimezone(pytz.timezone('US/Michigan'))) 
"""

""" 
# convert naive time to timezone aware
dt_eastern = datetime.datetime.now()
print(dt_eastern)
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_eastern)
print(dt_mtn) 
"""

# # format
# dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dt_mtn.strftime('%B %d, %Y'))

# # string to datetime
# dt_str = 'September 08, 2022'
# print(strptime(dt_str,'%B %d, %Y'))
