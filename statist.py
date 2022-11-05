import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stoloto.csv')

df = pd.DataFrame(data)

del df['Number']

a = df[['1']].value_counts()[:10]



print(a)

a.plot()
plt.show()

#1=87
#2=67,88,80,12
#3=23,13,3,8
#4=44
#5=59
#6=40,29,33,34,39
#7=41
