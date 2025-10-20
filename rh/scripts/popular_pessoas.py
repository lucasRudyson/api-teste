from faker import Faker
from rh.models import Pessoa
import random
import django
import os

# Só precisa da parte abaixo se rodar fora do shell do Django:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seuprojeto.settings')
django.setup()

fake = Faker('pt_BR')
for _ in range(45):
    cpf_bruto = fake.cpf()
    cpf_apenas_numeros = ''.join(filter(str.isdigit, cpf_bruto))
    Pessoa.objects.create(
        nome=fake.name(),
        cpf=cpf_apenas_numeros,
        email=fake.email(),
        telefone=''.join(filter(str.isdigit, fake.phone_number()))[:12],
        cidade=fake.city(),
        status=random.choice([True, False])
    )
print("Banco populado!")
