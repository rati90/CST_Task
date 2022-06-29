import asyncio
import typer

from db.db_setup import engine
from db.models import user, post


async def init_models():
    async with engine.begin() as conn:
        #await conn.run_sync(user.Base.metadata.drop_all)
        await conn.run_sync(user.Base.metadata.create_all)
        #await conn.run_sync(post.Base.metadata.drop_all)
        await conn.run_sync(post.Base.metadata.create_all)



cli = typer.Typer()


@cli.command()
async def db_init_models():
    await asyncio.run(init_models())
