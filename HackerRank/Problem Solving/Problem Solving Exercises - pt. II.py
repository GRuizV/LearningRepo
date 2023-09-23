import math
import itertools


'Encryption'


s = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
print(len(s))

columns = math.ceil(math.sqrt(len(s)))
print(f'ceil: {columns}')

rows = math.floor(math.sqrt(len(s)))
print(f'floor: {rows}')

if rows * columns < len(s):
    rows = columns


result, rows_words = list(), list()

for i in range(rows):
    rows_words.append(s[i*columns:i*columns+columns])
    
print(rows_words)


for i in range(columns):

    temp = str()

    for j in rows_words:

        if i > len(j)-1:
            continue
        
        temp += j[i]
    
    result.append(temp)

print(result)

result_string = str()

for i in result:
    
    result_string += i + ' '

result_string.rstrip()

print(result_string)
























