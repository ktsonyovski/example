from sqlalchemy import create_engine, Table, Column, MetaData, String

engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()
connection = engine.connect()

users_table = Table(
    "users",
    meta,
    Column("username", String, nullable=False),
    Column("password", String, nullable=False)
)

def create_user(username: str, password: str) -> None:
    add_user = users_table.insert().values(username=username, password=password)
    connection.execute(add_user)
    connection.commit()

def delete_user(username: str) -> None:
    del_user = users_table.delete().where(users_table.c.username == username)
    connection.execute(del_user)
    connection.commit()