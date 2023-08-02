

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print the date in the format "March 01, 2016"

# sentence = '{:%B %d, %Y}'.format(my_date)

# print the date in the format "March 01, 2016 fell on a Tuesday and was the 061 day of the year."

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

'''fStringed'''

new_sentence = f'{my_date:%B %d, %Y} fell on a {my_date:%A} and was the {my_date:%j} day of the year'

print(sentence)
print(new_sentence)