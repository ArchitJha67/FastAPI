## database.py imports (async)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(
    settings.database_url,  # database url is loaded from .env file
    echo=True,  # echo prints all the sql statements to the console
)

AsyncSessionLocal = async_sessionmaker(   #  Session Local is a transaction with the db
    engine,
    class_=AsyncSession,
    expire_on_commit=False           # Helps with issues of expired objects after commit (recommend for async)      
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session