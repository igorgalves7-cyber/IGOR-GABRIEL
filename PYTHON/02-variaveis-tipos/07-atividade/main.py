# Entrada de dados
nome = input('Digite seu nome: ')
ano_nascimento = input('Digite seu ano de nascimento: ')

# Verificando tipos recebidos
print(type(nome))
print(type(ano_nascimento))

# Conversão
ano_nascimento_int = int(ano_nascimento)

# Processamento
ANO_ATUAL = 2026
idade = ANO_ATUAL - ano_nascimento_int

# Saída formatada
print(f'Olá {nome}, sua idade é {idade} anos')