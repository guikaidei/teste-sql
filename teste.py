import os
import pymssql
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT", "1433")  # Default to 1433 if not set

try:
    conn = pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database,
        port=int(port) if port else 1433,
        login_timeout=5
    )
    cursor = conn.cursor()

    print("✅ Conexão estabelecida com sucesso (pymssql)!")
    cursor.execute("SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
    for row in cursor.fetchall():
        print(f"{row[0]}.{row[1]}")

    conn.close()
except Exception as e:
    print("❌ Erro:", e)
