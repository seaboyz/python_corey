import datetime

current_weight = 200
goal_weight = 180
avg_lbs_per_week = 2

# set start date as today
start_date = datetime.date.today()

# calculate end date
end_date = start_date + datetime.timedelta(weeks=(current_weight - goal_weight) / avg_lbs_per_week)

print("Start Date: {}".format(start_date))
print("End Date: {}".format(end_date))