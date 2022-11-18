from pydantic import BaseModel, EmailStr, constr
from datetime import datetime


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


class UserBaseSchema(BaseModel):
    id: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: str
    email: EmailStr
    name: str
