import pandas as pd

##TASK 1   WHICH JOB HAS THE HIGHEST SALARY?

df = pd.read_csv('Salary_Data.csv')
average_salry = df.groupby('Job Title')['Salary'].mean().reset_index()

final = average_salry.sort_values('Salary', ascending=False).reset_index(drop=True)
#.reset_index(drop = True) ==delete old indexs

print(final)


##TASK 2   CONTROL THE SALARIES, IS THERE INEQUALITY?(for genders)

df2 = pd.read_csv('Salary_Data.csv')

f= df2[df2['Gender'] == 'Female']
m= df2[df2['Gender'] == 'Male']

f2 = f.groupby('Job Title')['Salary'].mean().to_frame()
m2 = m.groupby('Job Title')['Salary'].mean().to_frame()

final_df = f2.join(m2, lsuffix='_salry', rsuffix='_salry')   #we are connecting the 2 different df.

final_df.columns = ['female salary', 'male salary']

final_df = final_df.reset_index()  #if we don't do it we don't have the 'job title summary.

final_df = final_df.sort_values('female salary', ascending=False)

final_df = final_df.reset_index(drop=True)

print(final_df)


