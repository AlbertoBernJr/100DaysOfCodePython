#Perform various operations on sets (union, intersection, etc.).

# Criando dois conjuntos com alguns números
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

"""
1. União
- A união junta todos os elementos de ambos os conjuntos, sem repetir 
    elementos.
- Existem duas formas de realizá-la: usando o método union() ou o 
    operador '|'.
"""
uniao = conjunto1.union(conjunto2)   
# ou: uniao = conjunto1 | conjunto2

print("União:", uniao)
# Resultado: {1, 2, 3, 4, 5, 6, 7, 8}

"""
2. Interseção
- A interseção retorna os elementos que estão presentes em ambos os 
    conjuntos.
- Também pode ser feita com o método intersection() ou com o operador '&'.
"""
intersecao = conjunto1.intersection(conjunto2)  
# ou: intersecao = conjunto1 & conjunto2

print("Interseção:", intersecao)
# Resultado: {4, 5}

"""
3. Diferença
- A diferença de um conjunto em relação a outro retorna os elementos que
    estão no primeiro conjunto, mas não no segundo.
- Usamos o método difference() ou o operador '-'.
"""
diferenca = conjunto1.difference(conjunto2)   
# ou: diferenca = conjunto1 - conjunto2

print("Diferença (conjunto1 - conjunto2):", diferenca)
# Resultado: {1, 2, 3}

"""
4. Diferença Simétrica
- A diferença simétrica retorna os elementos que estão em um dos conjuntos,
    mas não em ambos. É como pegar a soma das diferenças de cada conjunto.
- Use o método symmetric_difference() ou o operador '^'.
"""
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)   
# ou: conjunto1 ^ conjunto2

print("Diferença Simétrica:", diferenca_simetrica)
# Resultado: {1, 2, 3, 6, 7, 8}

"""
5. Verificando se um conjunto é subconjunto de outro
# Podemos verificar se todos os elementos de um conjunto estão contidos no outro.
"""
subconjunto = {4, 5}
resultado_subconjunto = subconjunto.issubset(conjunto1)
print("O subconjunto {} está contido em conjunto1? {}".format(subconjunto, resultado_subconjunto))
# Resultado: True
