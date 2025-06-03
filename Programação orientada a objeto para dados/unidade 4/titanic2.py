from dataprep import DataPrep
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, RocCurveDisplay
from sklearn.metrics import roc_auc_score

dp = DataPrep(df) 
df_treino, df_teste = dp.preparar_dados()

clf = LogisticRegression()  

 

X_treino = df_treino.drop(columns='Survived') 
y_treino = df_treino['Survived']  

X_teste = df_teste.drop(columns='Survived') 
y_teste = df_teste['Survived']


clf.score(I_teste, y_teste)	
y_previsto = clf.precict(X_teste) 
accuracy_score(y_teste, y_previsto)



df_fraude = pd.read_csv('trains_transaction.csv')
df_fraude.shape

df_fraude['isFraud'].value_counts(normalize=True)

y_previsto = clf.predict(X_teste) 

cm = confusion_matrix(y_teste, y_previsto)



y_proba = clt.predict_proba(X_teste)
y_proba = pd.DataFrame(y_proba)


tx_falso_positivo, tx_verdadeiro_positivo, _ = roc_curve(y_teste, y_proba[1])
ax = RocCurveDisplay(fpr=tx_falso_positivo, tpr=tx_verdadeiro_positivo).plot()

roc_auc_score(y_teste, y_previsto)