#Handle exceptions for division by zero

#[try-except] = bloco para lidar com o error [ZeroDivisionError]
try:
# bloco [try] = O código dentro do bloco é executado normalmente
# Se ocorrer uma divisão por zero, uma exceção [ZeroDivisionError] é ativada.

    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    print("----------------")
    resultado = numerador / denominador

except ZeroDivisionError:
#[ZeroDivisionError] = gerada pela divisão por zero
#Se a exceção [ZeroDivisionError] for ativada, o código dentro do bloco [except] será executado.
#Exibirá mensagem de erro
#Se houver error, o programa continua normalmente após o tratamento.

    print("Erro: Divisão por zero não é permitida.")
except ValueError:
#validando os dados antes executar a operação
#se o valor digitado não for um número, enviará a mensagem de [entrada inválida]

    print("Erro: Entrada inválida. Digite apenas números.")
else:
#[else] = código só será executado se nenhuma exceção for ativada

    print("Resultado:", resultado)
finally:
#[finally] = o código será executado independentemente de erros

    print("Fim do programa.")