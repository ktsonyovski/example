from sqlalchemy import create_engine, Table, Column, MetaData, String, text

engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()
connection = engine.connect()

users_table = Table(
    "users",
    meta,
    Column("username", String, nullable=False),
    Column("password", String, nullable=False)
)

def create_table():
    connection.execute(text("CREATE TABLE IF NOT EXISTS users (username string, password string)"))

def create_user(username: str, password: str) -> None:
    add_user_query = users_table.insert().values(username=username, password=password)
    connection.execute(add_user_query)
    connection.commit()

def delete_user(username: str) -> None:
    del_user_query = users_table.delete().where(users_table.c.username == username)
    connection.execute(del_user_query)
    connection.commit()

def get_all_users():
    get_users_query = connection.execute(text("SELECT * FROM users")) 
    return [dict(row._mapping) for row in get_users_query]