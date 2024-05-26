with name := <str>$name,
select(insert Category{
  name := name,
}){
  id,
  name
}