with full_name := <str>$full_name,
select(insert User{
  full_name := full_name
}){
  id,
  full_name
}