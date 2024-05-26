# AUTOGENERATED FROM 'app/queries/get_all_categories.edgeql' WITH:
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
class GetAllCategoriesResult(NoPydanticValidation):
    id: uuid.UUID
    name: str


async def get_all_categories(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetAllCategoriesResult]:
    return await executor.query(
        """\
        select Category{
          id,
          name
        }\
        """,
    )