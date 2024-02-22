import pandas as pd
from faker import Faker
import random

# Inicialize o Faker
fake = Faker('pt_BR')

# Lista para armazenar os dados
dados = []

# Gerar dados para 1000 alunos
for _ in range(1000):
    cpf = fake.unique.random_number(digits=11)
    nome = fake.name()
    idade = random.randint(18, 28)
    sexo = fake.random_element(elements=('M', 'F'))
    email = fake.email()
    nota_enem = random.randint(640, 800)
    abandono = fake.random_element(elements=(True, False))
    semestre = random.randint(1, 8) if abandono else None
    cra_segundo_semestre = random.uniform(5, 10)
    cra_quarto_semestre = random.uniform(5, 10)
    cra_sexto_semestre = random.uniform(5, 10)
    
    dados.append([cpf, nome, idade, sexo, email, nota_enem, abandono, semestre, cra_segundo_semestre, cra_quarto_semestre, cra_sexto_semestre])

# Criar DataFrame
df = pd.DataFrame(dados, columns=['CPF', 'Nome', 'Idade', 'Sexo', 'Email', 'Nota_ENEM', 'Abandono', 'Semestre', 'CRA_Segundo_Semestre', 'CRA_Quarto_Semestre', 'CRA_Sexto_Semestre'])

# Salvar DataFrame em um arquivo CSV
df.to_csv('dados_alunos.csv', index=False)

print("Dados salvos com sucesso em 'dados_alunos.csv'")
