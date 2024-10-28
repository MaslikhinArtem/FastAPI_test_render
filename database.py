from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_async_engine(
    'sqlite+aiosqlite///:tasks.db'
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class TasksOrm(DeclarativeBase):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    author: Mapped[str]