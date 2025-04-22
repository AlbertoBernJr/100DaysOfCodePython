"""
- Crie um chatbot usando bibliotecas NLP

- Instalando o NLTK = pip install nltk

- Como Funciona
O chatbot verifica a entrada do usuário e compara com os padrões definidos. 
Se encontrar uma correspondência, responde com uma das respostas associadas. 
Caso contrário, utiliza a resposta padrão informando que não entendeu.
"""

import nltk
#Importa a biblioteca NLTK

from nltk.chat.util import Chat, reflections
#Importa as classes necessárias para criar o chatbot.

#[pares]: Lista de pares contendo padrões (expressões regulares) e as 
#   respostas correspondentes.
pares = [
    [
        r"oi|olá|ei",
        ["Olá! Como posso ajudar você?", "Oi! Em que posso ser útil?"]
    ],
    [
        r"qual é o seu nome\??",
        ["Eu sou um chatbot simples criado com NLTK."]
    ],
    [
        r"como você está\??",
        ["Estou funcionando normalmente. E você?", "Tudo bem por aqui!"]
    ],
    [
        r"tchau|adeus",
        ["Tchau! Foi bom conversar com você.", "Até mais!"]
    ],
    [
        r"(.*)",
        ["Desculpe, não entendi. Pode reformular?"]
    ]
]

# Criar o chatbot
chatbot = Chat(pares, reflections)
#[Chat(pares, reflections)]: Cria uma instância do chatbot com os pares 
#   definidos e reflexões para substituir pronomes

# Iniciar a conversa
print("Olá! Digite algo para começar a conversar. (Digite 'sair' para encerrar)")
chatbot.converse()
#[chatbot.converse()]: Inicia a interação com o usuário.
