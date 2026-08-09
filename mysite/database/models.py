from .db import Base
from sqlalchemy import Integer, String, ForeignKey, Date, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from datetime import date, datetime
import enum

class StatusChoices(str, enum.Enum):
    admin = 'admin'
    student = 'student'
    teacher = 'teacher'

class UserProfile(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(150))
    username: Mapped[str] = mapped_column(String(150), unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.student)
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user',
                                                            cascade='all, delete-orphan')
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class RefreshToken(Base):
    __tablename__ = 'refresh_token'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)