import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

from sqlalchemy import create_engine

engine = create_engine(url=os.getenv('DB_URL'))
session_factory = sessionmaker(bind=engine)

def get_session():
    session = session_factory()
    yield session
    try:
        session.commit()
    except Exception as e:
        print(str(e))
    finally:
        session.close()