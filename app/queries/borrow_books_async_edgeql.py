# AUTOGENERATED FROM 'app/queries/borrow_books.edgeql' WITH:
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
class BorrowBooksResult(NoPydanticValidation):
    id: uuid.UUID


async def borrow_books(
    executor: edgedb.AsyncIOExecutor,
    *,
    is_borrowed: bool,
    borrower_id: uuid.UUID,
) -> list[BorrowBooksResult]:
    return await executor.query(
        """\
        with is_borrowed := <bool>$is_borrowed,
          borrower_id := <uuid>$borrower_id,

        select(update Book set{
          is_borrowed := is_borrowed,
          borrower := (Select User filter .id = borrower_id)
        }){
          id
        }\
        """,
        is_borrowed=is_borrowed,
        borrower_id=borrower_id,
    )
