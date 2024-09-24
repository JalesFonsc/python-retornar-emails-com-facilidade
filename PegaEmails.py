import re
import sys
# Passa a string de e-mails no segundo parâmetro;
emails = re.findall('\<(.*?)\>', 'De: Joziane França Gavassa <joziane.gavassa@rfm.com.br>Date: <joziane.gavassa@rfm.com.br> <joziane.gavassa@rfm.com.br>ter., 24 de set. de 2024 às 16:10Subject: Grand Lodge | LEMBRETE DE ENVIO DE DOCUMENTAÇÕES - AGOSTO 2024 - Não responda este email.To: <paula.menezes@solotrat.com.br>, Erick Suque Barbosa <erick.barbosa@rfm.com.br>, <construsantana291@gmail.com>, | EMPREITEIRA CHAVES <empreiteira_chaves@hotmail.com>, Juliema Datus <datusjuliema@gmail.com>, <guilherme@grupogks.com.br>, <fcsconstrucoes@yahoo.com>, Jeferson Simões <construsimoesempreiteiraltda@gmail.com>, <secretaria.premierpisos@gmail.com>, Juliano Nogueira Ubaldo <julianoubaldo76@gmail.com>, victor hiroshi pavao miyahara miyahara <vihpm@yahoo.com.br>, <davi@grupocamacon.com.br>Cc: Thais Daiane da Silva <thais.silva@rfm.com.br>, Aline da Guia Vaz <aline.vaz@rfm.com.br>, Sergio Pougy <sergio.pougy@rfm.com.br>, Thiago Leite <thiago.leite@rfm.com.br>')

# Conjunto joker para guardar os email-s sem repetição
emails_filtrados = set(emails)

# Verifica se não encontrou e-mails
if not emails_filtrados:
    print('Nenhum e-mail foi encontrado.')
else:
    # Imprime os e-mails filtrados, separados por vírgula
    print(', '.join(emails_filtrados))