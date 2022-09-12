from fileinput import filename
import logging
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = sub(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = mul(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = div(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
