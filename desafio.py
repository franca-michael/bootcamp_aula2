CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
#nome_usuario = input("Digite o seu nome: ")

# nome_usuario = 33 isso e um erro?

nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Voce digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Voce nao digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Voce digitou so espaco")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o seu salario: "))
try:
    salario_usuario = float(salario_usuario)
except ValueError:
    print("Salario invalido")
    exit()

if salario_usuario < 0:
    print("Salario nao pode ser negativo")
    exit()
elif salario_usuario == 0:
    print("Salario nao pode ser zero")
    exit()
elif salario_usuario is None:
    print("Salario nao pode ser vazio")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")