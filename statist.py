import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stoloto.csv')

df = pd.DataFrame(data)

del df['Number']

a = df[['1','2']].value_counts()



print(a)

# a.plot()
# plt.show()

#1=87
#2=67,88,80,12
#3=23,13,3,8
#4=44,1,62,89
#5=59
#6=40
