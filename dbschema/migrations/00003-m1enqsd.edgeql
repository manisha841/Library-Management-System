CREATE MIGRATION m1enqsdd2cahy46rb7xcrb7yrdln5wsguhxbwflatsnf3ewudw2z4q
    ONTO m1hxkeqhtf57a5lriexnrlum77uxqfqt4iehoivclbj6snjpyof4za
{
  ALTER TYPE default::Book {
      CREATE LINK borrower: default::User;
      CREATE PROPERTY is_borrowed: std::bool;
  };
  ALTER TYPE default::User {
      DROP LINK borrowed_books;
  };
};
