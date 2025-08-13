import pymssql

server = 'IP_DO_SERVIDOR'  # Ex: '192.168.0.10'
port = 1433
database = 'NOME_DA_BASE'
username = 'USUARIO'
password = 'SENHA'

try:
    conn = pymssql.connect(
        server=server,
        port=port,
        user=username,
        password=password,
        database=database,
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
