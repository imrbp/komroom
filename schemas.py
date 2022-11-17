from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    author_id: str
    post_id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author_id: str
    upvote: int
    downvote: int
    comments: list[Comment] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    id: str
    name: str
    email: str
    password: str


class User(UserBase):
    id: str
    name: str

    class Config:
        orm_mode = True
