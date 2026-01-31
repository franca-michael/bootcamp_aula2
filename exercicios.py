import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 + numero_02
print(resultado)


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Inserir um numero inteiro: "))
resto = numero % 5
print(resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 * numero_02
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Inserir um numero inteiro: "))
quadrado = numero ** 2
print(quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_01 = float(input("Inserir um numero flutuante: "))
numero_02 = float(input("Inserir outro numero flutuante: "))
resultado = numero_01 + numero_02
print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_01 = float(input("Inserir um numero flutuante: "))
numero_02 = float(input("Inserir outro numero flutuante: "))
media = (numero_01 + numero_02) / 2
print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Inserir a base (numero flutuante): "))
expoente = float(input("Inserir o expoente (numero flutuante): "))
potencia = base ** expoente
print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Inserir a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Inserir o raio do círculo: "))
area = math.pi * (raio ** 2)
print(area)


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Inserir uma frase: ")
texto_maiusculo = texto.upper()
print(texto_maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
texto = input("Inserir uma frase: ")
texto_minusculo = texto.lower()
print(texto_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
texto = input("Inserir uma frase: ")
texto_sem_espacos = texto.strip()
print(texto_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Inserir uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print(dia)
print(mes)
print(ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_01 = input("Inserir a primeira string: ")
string_02 = input("Inserir a segunda string: ")
concatenacao = string_01 + string_02
print(concatenacao)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação