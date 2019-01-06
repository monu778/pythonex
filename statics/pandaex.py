import numpy as np
import pandas as pd 
data = {
    'weekday':['Sun','Sun','Mon','Mon'],
    'city':['Austin','Dallas','Austin','Dallas'],
    'visitors':[139,237,326,456],
    'signups':[7,12,3,5]
}

users  = pd.DataFrame(data)

print(users)

cities = ['Austin','Dallas','Austin','Dallas']
signups = [7,12,3,5]
visitors = [139,237,326,456]
weekdays = ['Sun','Sun','Mon','Mon']
list_labels = ['cities','signups','visitors','weekday']
list_cols = [cities,signups,visitors,weekdays]
zipped=list(zip(list_labels,list_cols))
print(zipped)
data=dict(zipped)
users = pd.DataFrame(data)
print(users)

#Broadcasting
users['fees'] = 0 #broadcast to entire columns
print(users)
heights  = [59.0,65.2,62.9,65.4,63.7,65.7,64.1]
data = {'height':heights,'sex':'M'}
results = pd.DataFrame(data)
print(results)
results.index=['A','B','C','D','E','F','G']

print(results)

