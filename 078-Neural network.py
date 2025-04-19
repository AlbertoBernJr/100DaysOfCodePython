#Implemente uma rede neural usando TensorFlow ou PyTorch

#-----Implementação em TensorFlow-----
"""
TensorFlow (Keras):
-Simplicidade: Ideal para iniciantes ou projetos rápidos.
-Produtividade: Menos código para resultados funcionais.
"""
# instanlando TensorFlow= [ pip install tensorflow ]

import tensorflow as tf               
# 1. Importa TensorFlow 2.x
#Carrega a API do TensorFlow 2, que inclui Keras como interface de alto nível
import numpy as np                    
# 2. Importa NumPy para dados sintéticos
#Utilizado para criar vetores numéricos e adicionar ruído Gaussiano

# 3. Gera 100 pontos x e y=2x+1 com ruído
X = np.linspace(0, 10, 100)
#100 pontos igualmente espaçados entre 0 e 10
y = 2 * X + 1 + np.random.normal(0, 0.5, 100)
#relação linear com ruído de desvio padrão 0.5

# 4. Constroi modelo: uma única saída linear
model = tf.keras.Sequential([
#Sequential: empilha camadas em sequência
    tf.keras.layers.Dense(1, input_shape=[1])
    #Dense(1, input_shape=[1]): única unidade de saída, mapeando um valor de 
    # entrada para um valor de saída linear
])

# 5. Compila com otimizador SGD e MSE como função de perda
model.compile(
    optimizer='sgd',
    #optimizer='sgd': Stochastic Gradient Descent, simples e eficiente para 
    # problemas pequenos
    loss='mean_squared_error'
    #loss='mean_squared_error': erro quadrático médio, padrão em regressão
    
)

# 6. Treina por 20 épocas
history = model.fit(
    X, y,
    epochs=20,
    #epochs=20: realiza 20 passadas completas sobre os dados
    verbose=0
    #verbose=0: suprime logs para focar no resultado final
)

# 7. Exibe os pesos aprendidos (slope e intercept)
w, b = model.layers[0].get_weights()
#retorna [ [w], [b] ], onde w é o coeficiente angular (slope) e b o intercepto
print(f"Peso (w): {w[0][0]:.3f}, Viés (b): {b[0]:.3f}")

# 8. Faz previsões em novos pontos e plota o resultado
import matplotlib.pyplot as plt

plt.scatter(X, y, label="Dados originais")
#plt.scatter(...): plota os dados originais
plt.plot(X, model.predict(X), label="Ajuste pelo modelo")
#plt.plot(...): desenha a reta prevista pelo modelo após o treinamento

plt.legend()
plt.show()