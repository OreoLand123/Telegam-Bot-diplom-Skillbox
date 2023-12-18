from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class User(Base):

    """
    Модель описания юзера
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    date_of_register = Column(DateTime, nullable=False, default=datetime.now())

    log = relationship(
        "Log",
        back_populates="user",
        cascade="all",
    )

    def __repr__(self):
        return f"<User {self.id}>"


class Log(Base):

    """Модель описания лога пользователя"""

    __tablename__ = "log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("user.id"))
    url = Column(String(60), nullable=False)
    filter_name = Column(String(60), nullable=False)
    param = Column(String(60), nullable=False)
    arg_param = Column(String(60), nullable=False)
    value = Column(String(60), nullable=False)
    count_value = Column(Integer, nullable=False)
    date_of_log = Column(DateTime, nullable=False, default=datetime.now())
    status_request = Column(Integer, nullable=False)
    count_obj = Column(Integer, nullable=False)

    user = relationship("User", back_populates="log")

    def __repr__(self):
        return f"<Log {self.id}>"
