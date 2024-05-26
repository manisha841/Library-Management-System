from __future__ import annotations

from http import HTTPStatus
from typing import List
from uuid import UUID

import edgedb
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app import get_edgedb_client
from app.queries import (
    create_books_async_edgeql,
    create_category_async_edgeql,
    get_book_by_id_async_edgeql,
    get_books_by_category_async_edgeql,
    list_categories_async_edgeql,
)


router = APIRouter()


class CreateCategory(BaseModel):
    name: str


class CreateBooks(BaseModel):
    author: str
    title: str


@router.post("/categories/", status_code=HTTPStatus.CREATED)
async def create_categories(
    payload: CreateCategory,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        category_obj = await create_category_async_edgeql.create_category(
            client, name=payload.name
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={"error": f"Category '{payload.name}' already exists."},
        )
    return category_obj


@router.get("/categories", status_code=HTTPStatus.OK)
async def get_categories(
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    categories = await list_categories_async_edgeql.list_categories(executor=client)
    return categories


@router.post("/books/{category_id}", status_code=HTTPStatus.CREATED)
async def add_books(
    payload: CreateBooks,
    category_id: UUID,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        books = await create_books_async_edgeql.create_books(
            executor=client,
            author=payload.author,
            title=payload.title,
            category_id=category_id,
        )
    except edgedb.errors.MissingRequiredError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail={"error": str(e)}
        )
    return books


@router.get("/books/{category_id}", status_code=HTTPStatus.OK)
async def get_books(
    category_id: UUID, client: edgedb.AsyncIOClient = Depends(get_edgedb_client)
):
    books = await get_books_by_category_async_edgeql.get_books_by_category(
        client, category_id=category_id
    )
    return books


@router.get("/book/{book_id}/", status_code=HTTPStatus.OK)
async def get_book(
    book_id: UUID, client: edgedb.AsyncIOClient = Depends(get_edgedb_client)
):
    book = await get_book_by_id_async_edgeql.get_book_by_id(client, book_id=book_id)
    return book
