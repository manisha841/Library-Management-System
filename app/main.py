from __future__ import annotations

import functools

import edgedb
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import categories, books

from dotenv import load_dotenv
import os

load_dotenv()

EDGEDB_PORT = os.getenv("EDGEDB_PORT")
EDGEDB_HOST= os.getenv("EDGEDB_HOST")
EDGEDB_USER= os.getenv("EDGEDB_USER")
EDGEDB_PASSWORD= os.getenv("EDGEDB_PASSWORD")
EDGEDB_DB= os.getenv("EDGEDB_DB")
EDGEDB_TLS_CA= os.getenv("EDGEDB_TLS_CA")


async def setup_edgedb(app):
    client = app.state.edgedb = edgedb.create_async_client(
        host=EDGEDB_HOST,
        port=EDGEDB_PORT,
        user=EDGEDB_USER,
        password=EDGEDB_PASSWORD,
        database=EDGEDB_DB,
        tls_ca=EDGEDB_TLS_CA,
    )
    await client.ensure_connected()


async def shutdown_edgedb(app):
    client, app.state.edgedb = app.state.edgedb, None
    await client.aclose()


def create_app():
    app = FastAPI()

    app.on_event("startup")(functools.partial(setup_edgedb, app))
    app.on_event("shutdown")(functools.partial(shutdown_edgedb, app))

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(books.router)
    app.include_router(categories.router)

    return app


app = create_app()