#If you are using Python 2.7 or 3 and you want number of occurrences for each element:

from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
Counter(z)

#Output: 
#Counter({'blue': 3, 'red': 2, 'yellow': 1})

