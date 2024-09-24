import re
import sys
# Passa a string de e-mails no segundo parâmetro;
emails = re.findall('\<(.*?)\>', 'SUBSTITUA O TEXTO/EMAIL AQUI')

# Conjunto joker para guardar os email-s sem repetição
emails_filtrados = set(emails)

# Verifica se não encontrou e-mails
if not emails_filtrados:
    print('Nenhum e-mail foi encontrado.')
else:
    # Imprime os e-mails filtrados, separados por vírgula
    print(', '.join(emails_filtrados))