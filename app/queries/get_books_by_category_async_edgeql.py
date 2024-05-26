# AUTOGENERATED FROM 'app/queries/get_books_by_category.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler):
        # Pydantic 2.x
        from pydantic_core.core_schema import any_schema
        return any_schema()

    @classmethod
    def __get_validators__(cls):
        # Pydantic 1.x
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetBooksByCategoryResult(NoPydanticValidation):
    id: uuid.UUID
    author: str | None
    title: str
    category: GetBooksByCategoryResultCategory


@dataclasses.dataclass
class GetBooksByCategoryResultCategory(NoPydanticValidation):
    id: uuid.UUID


async def get_books_by_category(
    executor: edgedb.AsyncIOExecutor,
    *,
    category_id: uuid.UUID,
) -> list[GetBooksByCategoryResult]:
    return await executor.query(
        """\
        select Book{
          author,
          title,
          category,
        } filter .category.id = <uuid>$category_id\
        """,
        category_id=category_id,
    )