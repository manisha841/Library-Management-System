select Book{
  author,
  title,
  category:{
    name
  },
} filter .id = <uuid>$book_id