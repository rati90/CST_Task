import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp


class Role(enum.IntEnum):
    user = 1
    moderator = 2
    admin = 3


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(300), nullable=False)
    role = Column(Enum(Role))
    is_public = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True, server_default="true")

    profile = relationship("Profile", back_populates="owner", uselist=False)

    friends = relationship("Friends", secondary='user_friends', backref='followers')


class Profile(Timestamp, Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")


class Friends(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="friends")




