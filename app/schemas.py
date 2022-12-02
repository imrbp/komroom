from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import List


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


class FilteredUserResponse(UserBaseSchema):
    id: str


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


class CreatePostSchema(BaseModel):
    author_id: str
    content: str
    upvote: int
    downvote: int

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    id: str
    author_id: str
    content: str
    upvote: int
    downvote: int
    created_at: datetime
    updated_at: datetime


class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]
