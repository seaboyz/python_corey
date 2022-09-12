import datetime
import calendar

balance = 5000
interest_rate = 13 * .01
monthly_payment = 100

today = datetime.date.today()
days_till_end_of_month = calendar.monthrange(
    today.year, today.month)[1] - today.day

print("Today is: {}".format(today))
print("Days till end of month: {}".format(days_till_end_of_month))

# make the first payment ,calculate the interest and the new balance
balance -= monthly_payment
interest = balance * (interest_rate / 365) * days_till_end_of_month
balance += interest

print("Balance after first payment: {}".format(balance))

first_day_of_next_month = datetime.date(today.year, today.month+1, 1)

total_interest = interest
total_paid = monthly_payment

while balance > 0:
    if balance < monthly_payment:
        monthly_payment = balance
    # balance after the payment on first day of next month
    balance = balance - monthly_payment

    total_paid += monthly_payment

    # if the balance is negative, set it to zero
    if balance < 0:
        balance = 0
    else:
        balance = round(balance, 2)

    print("Payment made on: {}".format(first_day_of_next_month))
    print("Intest you will pay this month: {:.2f}".format(interest))

    # calculate the interest and add it to the balance
    days_in_next_month = calendar.monthrange(
        first_day_of_next_month.year, first_day_of_next_month.month)[1]

    interest = balance * (interest_rate / 365) * days_in_next_month
    balance += interest

    total_interest += interest

    # update the first day of next month
    first_day_of_next_month = first_day_of_next_month + \
        datetime.timedelta(days=days_in_next_month)

    

print("Total interest paid: {:.2f}".format(total_interest))
print("Total amount paid: {:.2f}".format(total_paid))
