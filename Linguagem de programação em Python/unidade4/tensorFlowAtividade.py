import tensorflow as tf


#O conjunto de dados MNIST é um conjunto de imagens de dígitos escritos à mão (0 a 9). 
# É frequentemente usado como um ponto de partida para o aprendizado de máquina. 

mnist = tf.keras.datasets.mnist

# x_train e x_test contêm as imagens, enquanto y_train e y_test contêm as etiquetas correspondentes.
# As imagens são normalizadas dividindo-se cada pixel por 255.0. 
# Isso coloca os valores dos pixels no intervalo [0, 1], facilitando o treinamento do modelo.
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten: converte a matriz bidimensional das imagens (28x28 pixels) em um vetor unidimensional.
# Dense(128, activation='relu'): camada densa com 128 neurônios e função de ativação ReLU.
# Dropout(0.2): regularização por abandono, desativando aleatoriamente 20% dos neurônios durante o treinamento, para evitar overfitting.
# Dense(10, activation='softmax'): camada de saída com 10 neurônios (um para cada dígito) e função de ativação softmax, 
# que produzirá uma distribuição de probabilidade sobre as classes.
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])


# O modelo é compilado com o otimizador 'adam', a função de perda 'sparse_categorical_crossentropy' 
# (adequada para problemas de classificação multiclasse) e a métrica de 'accuracy'.
# O modelo é treinado usando-se o conjunto de treinamento (x_train e y_train) por cinco épocas.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#O desempenho do modelo é avaliado utilizando-se o conjunto de teste (x_test e y_test), e os resultados, incluindo a perda e a precisão, são exibidos.
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)