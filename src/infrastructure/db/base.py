import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from infrastructure.config.db_config import db_settings
from dotenv import load_dotenv

import os
load_dotenv()

sync_engine = create_engine(
    url=db_settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

async_engine = create_async_engine(
    url=db_settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)


session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)
print('!!!!!!!!!!!!!')

class Base(DeclarativeBase):
    pass


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     print(res.scalar())
#
#
# async def get_version():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(res.scalar())
#
#
# asyncio.run(get_version())
