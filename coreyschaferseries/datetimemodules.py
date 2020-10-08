import datetime
import pytz

#Your choice of a date
d = datetime.date(2016, 7, 24)
# print(d)

#Today's Date
tday = datetime.date.today()
# print(tday) #can get year, day, etc.

#print(tday.isoweekday())
# Normal: Monday 0 Sunday 6
#Iso Week Day: Monday 1 Sunday 7

tdelta = datetime.timedelta(days=7)

#print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

# Days until my birthday
birthday = datetime.date(2020, 8, 30)

till_birthday = birthday - tday

#print(till_birthday.days) #total_seconds and other ones

dt = datetime.datetime(2020, 7, 26, 12, 30, 45, 100000)

tdelta = datetime.timedelta(days=7)

# print(dt + tdelta) #.year() and more

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2020, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# # dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# # print(dt_utcnow)

# dt_pst = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
# print(dt_pst)

# for tz in pytz.all_timezones:
#     print(tz)

