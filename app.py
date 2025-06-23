# Плохой код с секретом и уязвимостью
DB_PASSWORD = "admin123"  # 🔥 Секрет в коде!

def connect_database():
    # Уязвимость: SQL-инъекция
    query = "SELECT * FROM users WHERE id = " + user_input  # Опасно!
    return query
