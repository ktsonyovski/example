from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///database.db', echo=True)

# connection
conn = engine.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS users (username string, password string)"))
conn.commit()

# sessions
session = Session(engine)
session.execute(text("INSERT INTO users (username, password) VALUES ('admin', 'root');"))
session.commit()
