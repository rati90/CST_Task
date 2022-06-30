from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
from typing import Dict

from db.models.post import Post, Comments
from pydantic_schemas.posts import PostCreate


async def get_post(db: AsyncSession, post_id: int):
    query = select(Post).where(Post.id == post_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_posts(db: AsyncSession):
    query = select(Post)
    result = await db.execute(query)
    return result.scalars().all()


async def get_user_posts(db: AsyncSession, user_id: int):
    query = select(Post).where(Post.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_delete_post(db: AsyncSession, post_id: int):
    query = delete(Post).where(Post.id == post_id)
    await db.execute(query)

    return {"message": "deleted"}


async def get_update_post(
    db: AsyncSession, post_id: int, update_text: Dict[str, str]
):
    query = update(Post).where(Post.id == post_id).values(update_text)
    await db.execute(query)
    return {"message": "updated"}


async def create_post(db: AsyncSession, description: str, user_id: int):
    db_post = Post(
        description=description,
        user_id=user_id,
    )
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)

    return db_post


async def create_comment(db: AsyncSession, comment_text: str, post_id: int, user_id: id):
    db_comment = Comments(
        comment_text=comment_text,
        post_id=post_id,
        user_id=user_id

    )

    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)

    return db_comment

