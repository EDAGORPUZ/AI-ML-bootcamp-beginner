import pandas as pd

###CREATE YOUR OWN DATASET

students = [          
    {'name': 'eda', 'surname': 'görpüz', 'number': '123456'},
    {'name': 'oğuz', 'surname': 'ayhan', 'number': '1234'}
]

#ANOTHER VERSİON
# students = {
#     'name': ['eda', 'oğuz'],
#     'surname' : ['görpüz', 'ayhan'],
#     'number' : ['123456', '1234']
# }

df = pd.DataFrame(students)    #convert dataset to datafreame 
print(df)
print('\n')
print(df['surname'])   #print just the surname series
print(df[['name', 'surname']])  #if we want to print the 2 series we have to open the 2 brackets.
print(df.iloc[1])  #print 2nd row (iloc counts from the beginning)
print(df.loc[0])   #print 1st row (loc looks the index numbers)
print(df.shape)    #print the dimensions of the matrix 
print(df.head())   #print 5 row and head from beggining
print(df.info())   #print the informations for matrix
