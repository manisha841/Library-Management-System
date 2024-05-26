select Book{
  author,
  title,
  category,
} filter .category.id = <uuid>$category_id