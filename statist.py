import pandas as pd
import matplotlib.pyplot as plt

number_list=[]

data = pd.read_csv('stoloto.csv')

df = pd.DataFrame(data)

del df['Number']

a1 = df[['1']].value_counts()[:5]

a2 = df[['2']].value_counts()[:5]

a3 = df[['3']].value_counts()[:5]

a4 = df[['4']].value_counts()[:5]

a5 = df[['5']].value_counts()[:5]

a6 = df[['6']].value_counts()[:5]

a7 = df[['7']].value_counts()[:5]

print(a1,a2,a3,a4,a5,a6,a7)

a1.plot()
plt.show()

#1=87
#2=88
#3=3,23,8,13
#4=89,44
#5=59
#6=34
#7=41
