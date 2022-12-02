from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text, Table
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    post = relationship("Post", back_populates="author")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String)


Tags_map = Table(
    "association_table",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id")),
    Column("tag_id", ForeignKey("tags.id")),
)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(String, ForeignKey("users.id"))
    content = Column(String)
    upvote = Column(Integer)
    downvote = Column(Integer)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    author = relationship("User", back_populates="post")
    comments = relationship("Comment", back_populates="main_post")
    tags = relationship("Tag", secondary=Tags_map)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    author_id = Column(String, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    content = Column(String)

    main_post = relationship("Post", back_populates="comments")
