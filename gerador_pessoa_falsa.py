from faker import Faker
import random

# Função para gerar um CPF válido
def gerar_cpf():
    def calcular_digito(cpf_base):
        soma = sum([int(cpf_base[i]) * (len(cpf_base) + 1 - i) for i in range(len(cpf_base))])
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Gera os primeiros 9 dígitos
    cpf_base = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro e o segundo dígito verificador
    primeiro_digito = calcular_digito(cpf_base)
    cpf_base.append(primeiro_digito)
    segundo_digito = calcular_digito(cpf_base)
    cpf_base.append(segundo_digito)

    # Formata o CPF
    cpf_str = ''.join(map(str, cpf_base))
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"


# Inicializa o Faker com a localidade brasileira
fake = Faker('pt_BR')

def gerar_pessoa_falsa():
    nome_completo = fake.name()
    cpf_falso = gerar_cpf()
    email_falso = fake.email()
    endereco_completo = fake.address().replace("\n", ", ")  # Formata o endereço em uma linha
    telefone_falso = fake.phone_number()

    # Exibe os dados gerados
    print("Dados Gerados:\n")
    print(f"Nome Completo: {nome_completo}")
    print(f"CPF: {cpf_falso}")
    print(f"E-mail: {email_falso}")
    print(f"Endereço: {endereco_completo}")
    print(f"Telefone: {telefone_falso}")


if __name__ == "__main__":
    gerar_pessoa_falsa()
