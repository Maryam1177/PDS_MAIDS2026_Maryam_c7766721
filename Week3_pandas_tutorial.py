import pandas as pd
import seaborn as sns
df = sns.load_dataset('tips')
print(df.head())

#Task 1:

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

# 1- rows: 244, columns : 7
# 2- total_bill , tip , size
# 3- sex , day, time, smoker

#Task 2:
print(df[['total_bill', 'tip', 'day', 'time']].head())
print(df.iloc[0])
print(df.iloc[10:20])
print(df.loc[0:5, ['total_bill', 'tip']])

print(df.tail())
print(df.loc[20:30,['total_bill', 'size']])


#Task 4:
print(df[df['day'] == 'Sun'])
print(df[(df['day'] == 'Sun') & (df['total_bill'] > 20)])
print(df.query("day == 'Sun' and total_bill > 20"))

print(df[(df['time'] == 'Dinner') & (df['total_bill'] > 25)])
print(len(df[(df['time'] == 'Dinner') & (df['total_bill'] > 25)]))

#Task 5:
print(df.describe())
print(df.groupby('day')['tip'].mean())
print(df.groupby('sex')[['total_bill', 'tip']].mean())

# Sunday has the highest average tip.
print(df.groupby('time')['total_bill'].mean()) #Dinner


#1 - Selection chooses rows or columns by position or name.
# Filtering keeps only the rows that match a rule.

#2 - Query is shorter and read like a sentence.

# 3 - Sunday has the highest average tip.

# Tutorial 3.2 : Titanic case study

df = sns.load_dataset('titanic')
print(df.head())

# Task 1 :
print(df.shape)
print(df.columns)
print(df.head())
# survived

#Task 2:
print(df.isna().sum())
# age, deck, embarked, embark_town

#I filled missing ages with the median, so I don't lose 177 passengers.

#Task 3:
print(df.groupby ('sex')['survived'].mean())
print(df.groupby('class')['survived'].mean())
print(df.groupby('embark_town')['survived'].mean())

#Task 4:
print(len(df.query("sex =='female' and `class` =='First'"))) #94 Passengers.

print(df.query("age <16")['survived'].mean()) #0.5903614457831325

print(df.query("sex == 'male' and `class` =='Third'")['survived'].mean()) #0.13544668587896252

#Task 5 :
df['age_group']= 'adult'
df.loc[df['age']<16, 'age_group']='child'

print(df.groupby('age_group')['survived'].mean())

#Task 6 :
summary_table =df.groupby(['class','sex']) ['survived'].agg(['count','mean'])
print(summary_table.sort_values('mean', ascending=False))

# task 7:
final = df.groupby(['sex', 'class'])['survived'].agg(['count','mean']).reset_index()
final.columns = ['sex','class', 'passenger_count','survival-rate']
print(final.sort_values('survival-rate', ascending=False))



