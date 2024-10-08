import re

# Caso queira mudar os delimitadores, basta alterar o regex. Por padrão, deixei os delimitadres < >.
# Passa a string de e-mails no segundo parâmetro.
emails = re.findall('\<(.*?)\>', 'SUBSTITUA O TEXTO/EMAIL AQUI')

# Conjunto para guardar os email-s removendo as repetições caso haja.
emails_filtrados = set(emails)

# Verifica se não encontrou e-mails.
if not emails_filtrados:
    print('Nenhum e-mail foi encontrado.')
else:
    # Imprime os e-mails filtrados, separados por vírgula.
    print(', '.join(emails_filtrados))