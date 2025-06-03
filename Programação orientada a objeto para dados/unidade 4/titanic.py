import pandas as pd
from sklearn.linear_model import LogisticRegression 
from dataprep import DataPrep
from sklearn.feature_selection import RFECV 

df = pd.read_csv('train.csv')

df.head()

class DataPrep:

    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def remover_variaveis(self) -> None:
        colunas_para_remover = [
            'PassagerId',
            'Name',
            'Ticket'
            ]
        self.data.drop(columns=colunas_para_remover, inplace=True)

df.isna().sum() / df.shape[0]

df['Age'].median()

df.groupby(['Pclass', 'Sex'], as_index=False)['Age'].median()

X = df['Fare'].copy() 

X = X.values.reshape(-1, 1) 

y = df['Survived'].copy()

clf = LogisticRegression() 
clf.fit(X, y)
clf.predict_proba(np.array([[50]])) 
clf.predict_proba(np.array([[70]]))


dp = DataPrep(df)

df_traino, df_teste = dp.preparar_dados()
 

X_treino = df_treino.drop(columns='Survived')
y_treino = df_treino['Survived']
X_teste = df_teste.drop(columns='Survived')
y_teste = df_teste['Survived']

clf.fit(X_treino, y_teste)
clf.score(X_teste, y_teste)

seletor = RFECV(clf)  
seletor.fit(X_treino, y_treino)   

cols_indices = seletor.get_support(indices=True)  
cols = X_treino.columns[cols_indices]   
 

X_treino = X_treino[cols]  
X_teste = X_teste[cols]   

clf.fit(X_treino, y_treino) 
clf.score(X_teste, y_teste)