# AUTOGENERATED FROM 'app/queries/create_category.edgeql' WITH:
#     $ edgedb-py -d library


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
class CreateCategoryResult(NoPydanticValidation):
    id: uuid.UUID
    name: str


async def create_category(
    executor: edgedb.AsyncIOExecutor,
    *,
    name: str,
) -> CreateCategoryResult:
    return await executor.query_single(
        """\
        with name := <str>$name,
        select(insert Category{
          name := name,
        }){
          id,
          name
        }\
        """,
        name=name,
    )
