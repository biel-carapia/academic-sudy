import tensorflow as tf
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

#Dados de exemplo 

x_train = tf.constant([1.0], [2.0], [3.0], [4.0])
y_train = tf.constant([2.0], [4.0], [6.0], [8.0])

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

 

# Treinamento do modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

 

# Previsão
X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
print("Predição:", prediction[0][0])
plt.ylabel('Notas')
plt.show()