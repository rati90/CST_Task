from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import posts, users, login
from db.db_table_setup import cli, init_models


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Social Media",
        description="Social Media",
        version="0.0.1",
    )

    app.include_router(login.router)
    app.include_router(users.router)
    app.include_router(posts.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    @cli.command()
    async def db_init_models():
        await init_models()

    return app
