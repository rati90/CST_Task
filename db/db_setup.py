from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = (
    'sqlite+aiosqlite:///database.db'
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL) # echo=True

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)


Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
        await session.commit()
