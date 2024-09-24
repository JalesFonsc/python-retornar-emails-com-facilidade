import re
import sys
# Passa a string de e-mails no segundo parâmetro;
emails = re.findall('\<(.*?)\>', 'SUBSTITUA O TEXTO/E-MAIL AQUI')

# Conjunto joker para guardar os email-s sem repetição
emailsFiltrados = set()

# Remove os e-mails repetidos e joga no emailsFiltrados
def filtrar_Emails(email):
    if email in emailsFiltrados:
        return False
    emailsFiltrados.add(email)
    return True

# Listagem com os e-mails filtrados
filtradoEmailsRepetidos = list(filter(lambda x: filtrar_Emails(x), emails))

# Verifica se não encontrou e-mails e sai fora
if len(filtradoEmailsRepetidos) == 0:
    print('Nenhum e-mail foi encontrado')
    sys.exit()

for email in range(len(filtradoEmailsRepetidos)):
    emailAtual = filtradoEmailsRepetidos[email]

    # Verifica se é o último e-mail da listagem para não imprimir a vírgula;
    ultimoEmail = emailAtual == filtradoEmailsRepetidos[len(filtradoEmailsRepetidos) - 1]

    print(emailAtual if ultimoEmail else emailAtual + ', ')