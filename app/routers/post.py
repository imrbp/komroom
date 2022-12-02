from datetime import datetime
import uuid
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
from .. import oauth2


router = APIRouter()


@router.get("/")
def get_posts(
    db: Session = Depends(get_db),
    limit: int = 10,
    page: int = 1,
    search: str = "",
    user_id: str = Depends(oauth2.require_user),
):
    skip = (page - 1) * limit

    posts = db.query(models.Post).limit(limit).offset(skip).all()
    return {"status": "success", "results": len(posts), "posts": posts}


@router.post("/")
def create_post(
    db: Session = Depends(get_db),
    user_id: str = Depends(oauth2.require_user),
):
    return {user_id}
