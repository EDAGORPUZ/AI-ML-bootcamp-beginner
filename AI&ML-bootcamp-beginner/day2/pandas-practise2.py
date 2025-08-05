import pandas as pd

df = pd.read_csv('Salary_Data.csv')
print(df['Gender'] == 'Male')  #if gender=male True, if not False. So we are making mask.

print(df[df['Gender'] == 'Male'])  #it prints only true(male) options.
 
#if we want to make 2 filter:
print( df[ (df['Gender'] == 'Female') & (df['Job Title'] == 'Software Engineer') ])  

print(df[ ~ (df['Gender'] == 'Male')])  # ~ this symbol = not

#if we have a lot of filter: (we can check with the .isin method)
print(df[df['Job Title'].isin(['Senior Scientist', 'Senior Engineer', 'Social Media Specialist'])])

print(df [(df['Age'] >= 40 ) & (df['Gender'] == 'Female')])
print(df.sort_values('Age'))                    #ascending sort
print(df.sort_values('Age', ascending=False))   #descending sort

#if we want to see null options first:
print(df.sort_values('Age', ascending=False, na_position='first')) 

#if we want to automatic update we can inplace='True' parametre.

#if we want to sort 2 head:
print(df.sort_values(['Age', 'Years of Experience'], ascending=[False, False]))

df.sort_index() 

df.nlargest(10, 'Salary') #10 people with the highest salaries
df.nsmallest(10, 'Salary') #10 people with the lowest salaries

print( df.describe())  #some informations

a = pd.read_csv('Salary_Data.csv')
print(a['Gender'].value_counts())
# print(a['Gender'].value_counts(normalize=True))    ## calculate the  %ratio

print(df.groupby('Job Title')['Salary'].sum())  #make groups and sum the datas (sum, mean, median...)

