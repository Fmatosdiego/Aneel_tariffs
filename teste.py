# smtp_test.py

import smtplib
import config

print("Iniciando o teste de conexão SMTP.")

try:
    print("Conectando ao servidor SMTP...")
    server = smtplib.SMTP_SSL(config.smtp_server, config.smtp_port, timeout=10)
    print("Iniciando o login...")
    server.login(config.sender_email, config.sender_password)
    print("Conexão bem-sucedida.")
    server.quit()
except Exception as e:
    print(f"Erro de conexão: {e}")

print("Teste SMTP concluído.")
