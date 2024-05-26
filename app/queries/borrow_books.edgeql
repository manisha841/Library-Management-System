with is_borrowed := <bool>$is_borrowed,
  borrower_id := <uuid>$borrower_id,

select(update Book set{
  is_borrowed := is_borrowed,
  borrower := (Select User filter .id = borrower_id)
}){
  id
}