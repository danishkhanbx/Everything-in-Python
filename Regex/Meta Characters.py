from re import *
str = 'Example for Meta Characters in Regular Expression'
str1 = '123 Example for'
# res = findall('[a]', str)  # Output: ['a', 'a', 'a', 'a', 'a', 'a']
# res = findall('[in]', str)  # Output: ['i', 'n', 'i', 'n']
# res = findall('^Example', str)  # Output: ['Example']
# res = findall('^Meta', str)  # Output: []
# res = findall('Meta$', str)  # Output: []
# res = findall('ssion$', str)  # Output: ['ssion']
# res = findall('Exam...', str)  # Output: ['Example']
# res = findall('Exam.....', str)  # Output: ['Example f']
# res = findall('..Exam', str)  # Output: []
# res = findall('..r', str)  # Output: ['for', 'har', 'ter', 'lar', 'xpr']
# res = findall('am*', str)  # Output: ['am', 'a', 'a', 'a', 'a']
# res = findall('ss*', str)  # Output: ['s', 'ss']
# res = findall('m+', str)  # Output: ['m']
# res = findall('e{2}', str)  # Output: []
# res = findall('e{1}', str)  # Output: ['e', 'e', 'e', 'e', 'e']
# res = findall('\s', str)  # Output: [' ', ' ', ' ', ' ', ' ', ' ']
# res = findall('\S', str)  # Output: ['E', 'x', 'a', 'm', 'p', 'l', 'e', 'f', 'o', 'r', 'M', 'e', 't', 'a', 'C', 'h',
# 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', 'i', 'n', 'R', 'e', 'g', 'u', 'l', 'a', 'r', 'E', 'x', 'p', 'r', 'e', 's',
# 's', 'i', 'o', 'n']
# res = findall('\d', str1)  # Output: ['1', '2', '3']
# res = findall('\D', str1)  # Output: [' ', 'E', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 'f', 'o', 'r']
# res = findall('\w', str1)  # Output: ['1', '2', '3', 'E', 'x', 'a', 'm', 'p', 'l', 'e', 'f', 'o', 'r']
res = findall('\W', str)  # Output: [' ', ' ', ' ', ' ', ' ', ' ']
print(res)