from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, List

from api.services.auhontication import get_current_active_user
from api.utils.users import check_friendship
from db.db_setup import get_db
from pydantic_schemas.user import User
from pydantic_schemas.posts import Post
from api.utils.posts import (
    get_posts,
    get_post,
    get_delete_post,
    create_post,
    get_update_post, create_comment, get_user_posts
)

router = APIRouter(
    prefix="/posts",
    tags=["POSTS"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/create", response_model=Post, status_code=status.HTTP_201_CREATED
)
async def create_new_post(
        description: str,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    db_post = await create_post(db=db, description=description, user_id=current_user.id)
    return db_post


@router.get("/all", response_model=List[Post])
async def read_posts(db: AsyncSession = Depends(get_db)):
    posts = await get_posts(db=db)
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return posts


@router.get("/friends/posts")
async def read_friend_posts(friend_id: int,
                            current_user: User = Depends(get_current_active_user),
                            db: AsyncSession = Depends(get_db)
                            ):
    check_friend_status = await check_friendship(db=db, current_user=current_user.id, friend_id=friend_id)
    if check_friend_status:
        db_post = await get_user_posts(db=db, user_id=friend_id)
        return db_post
    else:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Non friend can not see the posts")


@router.get("/{post_id}")
async def read_post(post_id: int, db: AsyncSession = Depends(get_db)):
    db_post = await get_post(db=db, post_id=post_id)

    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return db_post


@router.patch("/{post_id}")
async def update_post(
        post_id: int,
        update_text: Dict[str, str],
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    db_post = await get_post(db=db, post_id=post_id)
    if db_post and db_post.user_id == current_user.id:
        return await get_update_post(
            db=db,
            post_id=post_id,
            update_text=update_text
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{post_id}")
async def delete_post(post_id: int,
                      db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_active_user)):
    db_post = await get_post(db=db, post_id=post_id)
    if db_post and db_post.user_id == current_user.id:
        return await get_delete_post(db=db, post_id=post_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/{post_id}/comments")
async def post_comment(post_id: int,
                       comment_text: str,
                       db: AsyncSession = Depends(get_db),
                       current_user: User = Depends(get_current_active_user)):
    db_post = await get_post(db=db, post_id=post_id)
    if db_post:
        if current_user.id == db_post.user_id:
            return await create_comment(db=db, post_id=post_id, comment_text=comment_text, user_id=current_user.id)

        check_friend_status = await check_friendship(friend_id=db_post.user_id, current_user=current_user.id, db=db)
        if check_friend_status:
            return await create_comment(db=db, post_id=post_id, comment_text=comment_text, user_id=current_user.id)
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Non friend can not post")

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post")
