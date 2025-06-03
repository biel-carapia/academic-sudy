import pandas as pd

df = pd.read_csv('exemplo.csv')

df.to_csv('exemplo.csv')
df.to_excel('exemplo.xlsx')

df=pd.read_pickle('exemplo.pkl')

df.to_pickle('exemplo2.pkl')