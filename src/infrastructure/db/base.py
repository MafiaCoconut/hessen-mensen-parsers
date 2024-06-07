from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os
load_dotenv()

engine = create_engine(
    url=os.getenv('DATABASE_URL'),
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(res.scalar())
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
