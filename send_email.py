import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def send_email(subject, body, recipient_email, sig_agente_info):
    sender_email = config.sender_email
    sender_password = config.sender_password

    # Configuração do servidor SMTP
    smtp_server = config.smtp_server
    smtp_port = config.smtp_port  # Certifique-se de que esta porta é 465 para SSL

    # Criar mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body += f"\n\nInformações adicionais: {sig_agente_info}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
