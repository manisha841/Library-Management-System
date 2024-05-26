with author := <str>$author,
    title := <str>$title,
select(insert Book{
  author := author,
  title := title,
  category := (Select Category {id} filter .id = <uuid>$category_id)
}){
  id,
  title,
  author,
  category:{
    name,
  }
}