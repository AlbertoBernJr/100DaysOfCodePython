"""
Execute tarefas de processamento de linguagem natural (por exemplo, análise 
de sentimento)
"""

# Instalação das bibliotecas = [ pip install tf-keras ]+[ pip install transformers torch ]

from transformers import pipeline

# Carregar o pipeline de análise de sentimento (usando um modelo BERT pré-treinado)
classificador = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
"""
[ pipeline("sentiment-analysis") ]:
- Carrega automaticamente um modelo pré-treinado para análise de sentimento.
- O modelo usado (distilbert-base-uncased-finetuned-sst-2-english) é uma versão otimizada do BERT, treinada no dataset SST-2

Processamento Automático:
- Tokenização: Converte o texto em tokens compatíveis com o BERT.
- Inferência: Executa o modelo para prever o sentimento.
- Pós-processamento: Converte a saída do modelo em rótulos (POSITIVE/NEGATIVE) e confiança

Resultados:
- Cada texto é classificado com um rótulo e uma pontuação de confiança entre 0 e 1
"""

# Textos para análise
textos = [
    "I love programming, it's amazing!",
    "This movie was terrible and boring.",
    "The product is okay, but the delivery was late."
]

# Realizar a análise
resultados = classificador(textos)

# Exibir os resultados
for texto, resultado in zip(textos, resultados):
    print(f"Texto: {texto}")
    print(f"Sentimento: {resultado['label']} (Confiança: {resultado['score']:.4f})\n")

"""
Tokenização:
- O texto é dividido em tokens (ex: ["I", "love", "programming", ...]).
- Tokens especiais como [CLS] (início) e [SEP] (fim) são adicionados.

Modelo BERT:
- Processa os tokens e gera um vetor de saída.
- A camada de classificação final mapeia esse vetor para os rótulos de sentimento.

Pós-Processamento:
- A função softmax converte os logits em probabilidades.
- A classe com maior probabilidade é escolhida como resultado
"""