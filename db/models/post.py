from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .user import User
from .mixins import Timestamp


class Post(Timestamp, Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    comments = relationship("Comments", back_populates='post', uselist=True)
    created_by = relationship(User)


class Comments(Timestamp, Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment_text = Column(String(200), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    post = relationship("Post", back_populates="comments")


