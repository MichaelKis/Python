import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stoloto.csv')

df = pd.DataFrame(data)

del df['Number']

a = df[['1','2','3','4','5']]

df['new_column'] = df['1'] + df['2']


#
# for x in range(1,31):
#
#     a = df[str(x)].value_counts()
#
print(a)
print(df['new_column'])

# a.plot()
# plt.show()
