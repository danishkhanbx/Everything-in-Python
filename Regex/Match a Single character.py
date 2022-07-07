from re import *

str = '12345'
print('Matches:', len(findall('\d', str)))
print('Matches:', len(findall('\D', str)))
print('Matches:', len(findall('\d{5}', str)))


nums = '123 1234 12345 123456 1234567'
print('Matches:', len(findall('\d{5,7}', nums)))
